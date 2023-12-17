use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashSet;
// use std::collections::BTreeMap;
use std::cmp::min;

struct Plane {
    map: Vec<Vec<char>>,
    i: usize,
    ii: usize
}

impl Plane {
    fn new() -> Plane {
        Plane {
            map: Vec::new(),
            i: 0,
            ii: 0
        }
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
    fn gravity_all_column(&mut self) {
        for ii in 0..self.ii {
            self.gravity_column(ii);
        }
    }
    fn gravity_column(&mut self, column_number: usize) {
        let mut rock_count = 0;
        for i in (0..self.map.len()).rev() {
            if let Some(row)  = self.map.get_mut(i) {
                if let Some(cc) = row.get_mut(column_number) {
                    if *cc == 'O' {
                        *cc = '.';
                        rock_count+=1;
                    }
                    else if *cc == '#' {
                        self.fill_in_rocks(column_number, i+1, rock_count);
                        rock_count = 0;
                    }
                }
            }
        }
        self.fill_in_rocks(column_number,0,rock_count);
    }
    fn fill_in_rocks(&mut self, column: usize, row: usize, number: usize) {
        for i in 0..number {
            if let Some(row) = self.map.get_mut(i+row) {
                if let Some(cc) = row.get_mut(column) {
                    *cc = 'O';
                }
            }
        }
    }
    fn count(&self, row: usize) -> usize {
        let mut cnt = 0;
        if let Some(r) = self.map.get(row) {
            for i in r.iter() {
                if *i == 'O' {
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
    fn score(&self) -> usize {
        let mut score = 0;
        for i in 0..self.i {
            score+= (self.i-i) * self.count(i);
        }
        return score;
    }
    fn print(&self) {
        for row in self.map.iter() {
            for c in row.iter() {
                print!("{}",c);
            }
            println!("");
        }
    }
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
    plane.gravity_all_column();
    plane.print();
    println!("Total Weight is: {}",plane.score());
    Ok(())
}