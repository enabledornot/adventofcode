use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use std::collections::BTreeMap;

#[derive(Clone)]
struct Mapping {
    a: [usize; 2],
    b: [usize; 2],
    dist: i64,
    is_start: bool
}

impl Mapping {
    fn new(c: char, i: usize, ii: usize) -> Mapping {
        match c {
            '|' => Mapping {a: [i.wrapping_sub(1),ii], b: [i+1,ii], dist: -1, is_start: false},
            '-' => Mapping {a: [i,ii.wrapping_sub(1)], b: [i,ii+1], dist: -1, is_start: false},
            'L' => Mapping {a: [i.wrapping_sub(1),ii], b: [i,ii+1], dist: -1, is_start: false},
            'J' => Mapping {a: [i,ii.wrapping_sub(1)], b: [i.wrapping_sub(1),ii], dist: -1, is_start: false},
            '7' => Mapping {a: [i+1,ii], b: [i,ii.wrapping_sub(1)], dist: -1, is_start: false},
            'F' => Mapping {a: [i,ii+1], b: [i+1,ii], dist: -1, is_start: false},
            '.' => Mapping {a: [i,ii], b:[i,ii], dist: -1, is_start: false},
            'S' => Mapping {a: [i,ii], b:[i,ii], dist: 0, is_start: true},
            _ => Mapping {a: [i,ii], b: [i,ii], dist: -1, is_start: false}
        }
    }
    fn find_other(&mut self, position: [usize; 2]) -> Option<[usize; 2]> {
        if position==self.a {
            return Some(self.b);
        }
        else if position==self.b {
            return Some(self.a);
        }
        return None
    }
}

struct Array_Map {
    map: Vec<Vec<Mapping>>,
    start: [usize; 2],
    max: usize
}

impl Array_Map {
    fn new() -> Array_Map {
        return Array_Map{map: Vec::new(), start: [usize::MAX,usize::MAX], max:usize::MAX};
    }
    fn add_item(&mut self, c: char) {
        let i = self.map.len()-1;
        if let Some(last_row) = self.map.last_mut() {
            let ii = last_row.len();
            if c=='S' {
                self.start = [i,ii];
            }
            last_row.push(Mapping::new(c,i,ii));
        }
    }
    fn add_line(&mut self) {
        self.map.push(Vec::new());
    }
    fn get_position(&mut self, pos: [usize;2]) -> Option<&mut Mapping> {
        if let Some(selected_row) = self.map.get_mut(pos[0]) {
            if let Some(selected_element) = selected_row.get_mut(pos[1]) {
                return Some(selected_element);
            }
        }
        return None;
    }
    fn traverse(&mut self) -> i32 {
        let mut seen: HashSet<[usize; 2]> = HashSet::new();
        seen.insert([self.start[0],self.start[1]]);
        let mut to_traverse: Vec<[usize; 2]> = Vec::new();
        to_traverse.push([self.start[0]+1,self.start[1]]);
        to_traverse.push([self.start[0].wrapping_sub(1),self.start[1]]);
        to_traverse.push([self.start[0],self.start[1]+1]);
        to_traverse.push([self.start[0],self.start[1].wrapping_sub(1)]);
        let mut count = 0;
        loop {
            if to_traverse.len()==0 {
                break;
            }
            let mut new_trans: Vec<[usize; 2]> = Vec::new();
            for position in &to_traverse {
                if let Some(current_pos) = self.get_position(*position) {
                    if let Some(new_pos) = current_pos.clone().find_other(*position) {
                        if ! seen.contains(&new_pos) {
                            new_trans.push(new_pos);
                        }
                    }
                }
            }
            count+=1;
            seen.extend(to_traverse);
            to_traverse = new_trans;
        }
        return count;
    }
    fn max_loop(&mut self) -> i32 {
        let mut to_traverse: Vec<[usize; 2]> = Vec::new();
        to_traverse.push([self.start[0]+1,self.start[1]]);
        to_traverse.push([self.start[0].wrapping_sub(1),self.start[1]]);
        to_traverse.push([self.start[0],self.start[1]+1]);
        to_traverse.push([self.start[0],self.start[1].wrapping_sub(1)]);
        let mut max = 0;
        for travel in to_traverse {
            let current = self.follow(self.start, travel);
            if current > max {
                max = current;
            }
        }
        return max;
    }
    fn follow(&mut self, position: [usize; 2], direction: [usize; 2]) -> i32 {
        let mut a_pos = position;
        let mut b_pos = direction;
        let mut count = 0;
        while let Some(&mut ref mut mappr) = self.get_position(b_pos) {
            println!("{:?}-{:?}",a_pos,b_pos);
            if let Some(new_pos) = mappr.find_other(a_pos) {
                a_pos = b_pos;
                b_pos = new_pos;
            }
            else {
                println!("ERROR");
                break;
            }
            count+=1;
        }
        println!("Count: {}",count);
        return count;
    }
}

// fn mapping_from_char(c: char, i: usize, ii: usize) -> Mapping {
//     match c {
//         '|' => Mapping {a: [i,ii.wrapping_sub(1)], b: [i,ii+1], dist: -1, is_start: false},
//         '-' => Mapping {a: [i.wrapping_sub(1),ii], b: [i+1,ii], dist: -1, is_start: false},
//         'L' => Mapping {a: [i,ii.wrapping_sub(1)], b: [i+1,ii], dist: -1, is_start: false},
//         'J' => Mapping {a: [i,ii.wrapping_sub(1)], b: [i.wrapping_sub(1),ii], dist: -1, is_start: false},
//         '7' => Mapping {a: [i.wrapping_sub(1),ii], b: [i,ii.wrapping_sub(1)], dist: -1, is_start: false},
//         'F' => Mapping {a: [i,ii+1], b: [i+1,ii], dist: -1, is_start: false},
//         '.' => Mapping {a: [i,ii], b:[i,ii], dist: -1, is_start: false},
//         'S' => Mapping {a: [i,ii], b:[i,ii], dist: -1, is_start: true}
//     }
// }

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut am = Array_Map::new();
    for str in read.lines() {
        let line = str?;
        am.add_line();
        for c in line.chars() {
            am.add_item(c);
        }
    }
    let max_dist = am.max_loop();
    println!("MAX distance: {}",max_dist/2 + 1);
    Ok(())
}