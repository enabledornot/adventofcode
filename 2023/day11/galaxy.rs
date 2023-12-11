use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

#[derive(Clone)]
struct Galaxy {
    position: [usize; 2]
}

impl Galaxy {
    fn single_dem_dist(a: usize, b: usize, x_lanes: &HashSet<usize>) -> usize {
        let mx = a.max(b);
        let mn = a.min(b);
        return (mx-mn) + (*x_lanes).iter().filter(|&x| *x > mn && *x < mx).count();
    }
    fn dist_to(&self, other_galaxy: &Galaxy, i_lanes: &HashSet<usize>, ii_lanes: &HashSet<usize>) -> usize {
        return Self::single_dem_dist(self.position[0],other_galaxy.position[0],i_lanes) + Self::single_dem_dist(self.position[1],other_galaxy.position[1],ii_lanes);
    }
}



fn find_expand(galaxy_list: &mut Vec<Galaxy>, direction: usize) -> HashSet<usize> {
    let mut current_lane: usize = 0;
    let mut free_lanes: HashSet<usize> = HashSet::new();
    galaxy_list.sort_by(|a, b| a.position[direction].cmp(&b.position[direction]));
    for item in galaxy_list.iter() {
        while item.position[direction] > current_lane {
            free_lanes.insert(current_lane);
            current_lane+=1;
        }
        current_lane = item.position[direction]+1;
    }
    return free_lanes;
}

fn sum_of_all_dist(mut galaxy_list: Vec<Galaxy>, i_lanes: &HashSet<usize>, ii_lanes: &HashSet<usize>) -> usize {
    if let Some(first) = galaxy_list.first().cloned() {
        let mut cnt = 0;
        for other_galaxy in &mut galaxy_list[1..] {
            cnt+=other_galaxy.dist_to(&first,i_lanes,ii_lanes);
        }
        return cnt + sum_of_all_dist(galaxy_list[1..].to_vec(),i_lanes,ii_lanes);
    }
    else {
        return 0;
    }
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut galaxy_list: Vec<Galaxy> = Vec::new();
    for (i,str) in read.lines().enumerate() {
        let line = str?;
        for (ii,c) in line.chars().enumerate() {
            if c=='#' {
                galaxy_list.push(Galaxy {
                    position: [i,ii]
                });
            }
        }
    }
    let i_lanes = find_expand(&mut galaxy_list,0);
    let ii_lanes = find_expand(&mut galaxy_list,1);
    let sum = sum_of_all_dist(galaxy_list, &i_lanes,&ii_lanes);
    println!("{}",sum);
    Ok(())
}