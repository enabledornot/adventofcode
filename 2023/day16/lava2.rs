use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
// use std::collections::BTreeMap;
use std::cmp::min;

#[derive(Eq, Hash, PartialEq, Clone)]
struct Beam {
    direction: [i32; 2],
    position: [i32; 2]
}

impl Beam {
    fn moved(&self,mut direct: [i32; 2]) -> Beam {
        if direct == [0,0] {
            direct = self.direction;
        }
        return Beam {direction: direct, position: [self.position[0] + direct[0], self.position[1] + direct[1]]};
    }
}

struct Plane {
    map: Vec<Vec<char>>,
    i: usize,
    ii: usize,
    seen: HashSet<[i32; 2]>,
    seendir: HashSet<Beam>
}

impl Plane {
    fn new() -> Plane {
        Plane {
            map: Vec::new(),
            i: 0,
            ii: 0,
            seen: HashSet::new(),
            seendir: HashSet::new()
        }
    }
    fn reset(&mut self) {
        self.seen = HashSet::new();
        self.seendir = HashSet::new();
    }
    fn add_row(&mut self) {
        self.i+=1;
        self.map.push(Vec::new());
    }
    fn add_char(&mut self, c: char) {
        if self.map.len()==1 {
            self.ii+=1;
        }
        if let Some(last) = self.map.last_mut() {
            last.push(c);
        }
    }
    fn print(&self) {
        for (i,row) in self.map.iter().enumerate() {
            for (ii,c) in row.iter().enumerate() {
                // println!("{:?}",[i as i32,ii as i32]);
                if self.seen.contains(&[i as i32,ii as i32]) {
                    print!("#");
                }
                else {
                    print!("{}",c);
                }
            }
            println!("");
        }
    }
    fn lookup_position(&self, position: [i32; 2]) -> Option<char> {
        if let Some(row) = self.map.get(position[0] as usize) {
            if let Some(c) = row.get(position[1] as usize) {
                return Some(*c);
            }
        }
        return None;
    }
    fn move_beam(&mut self, b: Beam) -> Vec<Beam> {
        let mut beams: Vec<Beam> = Vec::new();
        if let Some(c) = self.lookup_position(b.position) {
            self.seen.insert(b.position);
            match c {
                '.' => beams.push(b.moved([0,0])),
                '/' => beams.push(b.moved([b.direction[1]*-1,b.direction[0]*-1])),
                '\\' => beams.push(b.moved([b.direction[1],b.direction[0]])),
                '|' => {
                    if b.direction[1] != 0 {
                        beams.push(b.moved([-1,0]));
                        beams.push(b.moved([1,0]));
                    }
                    else {
                        beams.push(b.moved([0,0]));
                    }
                },
                '-' => {
                    if b.direction[0] != 0 {
                        beams.push(b.moved([0,-1]));
                        beams.push(b.moved([0,1]));
                    }
                    else {
                        beams.push(b.moved([0,0]));
                    }
                }
                _ => {
                    
                }
            }
        }
        beams.retain(|x| !self.seendir.contains(x));
        self.seendir.extend(beams.clone());
        return beams;
    }
}

fn calculate_visited(plane: &mut Plane, s_b : Beam) -> usize {
    plane.reset();
    let mut beam_list: Vec<Beam> = Vec::new();
    beam_list.push(s_b);
    while let Some(current) = beam_list.pop() {
        beam_list.extend(plane.move_beam(current));
    }
    return plane.seen.len();
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut plane = Plane::new();
    for str in read.lines() {
        let line = str?;
        plane.add_row();
        for c in line.chars() {
            plane.add_char(c);
        }
    }
    let mut max = 0;
    let imax = plane.i as i32;
    let iimax = plane.ii as i32;
    for v in 0..plane.i {
        let i = v as i32;
        let current = calculate_visited(&mut plane, Beam{direction: [0,1], position: [i,0]});
        if current > max {
            max = current;
        }
        let current2 = calculate_visited(&mut plane, Beam{direction: [0,-1], position: [i,iimax-1]});
        if current2 > max {
            max = current2;
        }
    }
    for v in 0..plane.ii {
        let i = v as i32;
        let current = calculate_visited(&mut plane, Beam{direction: [1,0], position: [0,i]});
        if current > max {
            max = current;
        }
        let current2 = calculate_visited(&mut plane, Beam{direction: [-1,0], position: [imax-1,i]});
        if current2 > max {
            max = current2;
        }
    }
    println!("Max visited: {}",max);
    Ok(())
}