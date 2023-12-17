use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashSet;
use std::collections::BTreeMap;
use std::cmp::min;

struct Plane {
    map: Vec<Vec<char>>,
    i: usize,
    ii: usize,
    cache: BTreeMap<Vec<Vec<char>>,i64>
}

impl Plane {
    fn new() -> Plane {
        Plane {
            map: Vec::new(),
            i: 0,
            ii: 0,
            cache: BTreeMap::new()
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
    fn cycle(&mut self) {
        self.gravity_all_column_north();
        self.gravity_all_column_west();
        self.gravity_all_column_south();
        self.gravity_all_column_east();
    }
    fn cycle_cnt(&mut self, cnt: i64) {
        let mut current_cycle = 0;
        while current_cycle < cnt {
            if let Some(last_seen) = self.cache.get(&self.map) {
                if 2*current_cycle - last_seen < cnt {
                    current_cycle += ((cnt - current_cycle) / (current_cycle - last_seen)) * (current_cycle - last_seen);
                }
                else {
                    while current_cycle < cnt {
                        self.cycle();
                        current_cycle += 1;
                    }
                }
            }
            else {
                self.cache.insert(self.map.clone(),current_cycle);
                self.cycle();
                current_cycle += 1;
            }
        }
    }
    fn gravity_all_column_east(&mut self) {
        for ii in 0..self.ii {
            self.gravity_column_east(ii);
        }
    }
    fn gravity_column_east(&mut self, row_number: usize) {
        let mut rock_count = 0;
        if let Some(row) = self.map.get_mut(row_number) {
            for ii in (0..self.ii) {
                if let Some(cc) = row.get_mut(ii) {
                    if *cc == 'O' {
                        *cc = '.';
                        rock_count+=1;
                    }
                    else if *cc == '#' {
                        if ii != 0 {
                            Plane::fill_in_rocks_east(row, ii-1, rock_count);
                            rock_count = 0;
                        }
                    }
                }
            }
            Plane::fill_in_rocks_east(row,self.ii-1,rock_count);
        }
    }
    fn fill_in_rocks_east(row: &mut Vec<char>, column: usize, number: usize) {
        for ii in 0..number {
            if let Some(cc) = row.get_mut(column-ii) {
                *cc = 'O';
            }
        }
    }
    fn gravity_all_column_south(&mut self) {
        for ii in 0..self.ii {
            self.gravity_column_south(ii);
        }
    }
    fn gravity_column_south(&mut self, column_number: usize) {
        let mut rock_count = 0;
        for i in (0..self.map.len()) {
            if let Some(row)  = self.map.get_mut(i) {
                if let Some(cc) = row.get_mut(column_number) {
                    if *cc == 'O' {
                        *cc = '.';
                        rock_count+=1;
                    }
                    else if *cc == '#' {
                        if i!=0 {
                            self.fill_in_rocks_south(column_number, i-1, rock_count);
                            rock_count = 0;
                        }
                    }
                }
            }
        }
        self.fill_in_rocks_south(column_number,self.map.len()-1,rock_count);
    }
    fn fill_in_rocks_south(&mut self, column: usize, row: usize, number: usize) {
        for i in 0..number {
            if let Some(row) = self.map.get_mut(row-i) {
                if let Some(cc) = row.get_mut(column) {
                    *cc = 'O';
                }
            }
        }
    }
    fn gravity_all_column_west(&mut self) {
        for ii in 0..self.ii {
            self.gravity_column_west(ii);
        }
    }
    fn gravity_column_west(&mut self, row_number: usize) {
        let mut rock_count = 0;
        if let Some(row) = self.map.get_mut(row_number) {
            for ii in (0..self.ii).rev() {
                if let Some(cc) = row.get_mut(ii) {
                    if *cc == 'O' {
                        *cc = '.';
                        rock_count+=1;
                    }
                    else if *cc == '#' {
                        Plane::fill_in_rocks_west(row, ii+1, rock_count);
                        rock_count = 0;
                    }
                }
            }
            Plane::fill_in_rocks_west(row,0,rock_count);
        }
    }
    fn fill_in_rocks_west(row: &mut Vec<char>, column: usize, number: usize) {
        for ii in 0..number {
            if let Some(cc) = row.get_mut(ii+column) {
                *cc = 'O';
            }
        }
    }
    fn gravity_all_column_north(&mut self) {
        for ii in 0..self.ii {
            self.gravity_column_north(ii);
        }
    }
    fn gravity_column_north(&mut self, column_number: usize) {
        let mut rock_count = 0;
        for i in (0..self.map.len()).rev() {
            if let Some(row)  = self.map.get_mut(i) {
                if let Some(cc) = row.get_mut(column_number) {
                    if *cc == 'O' {
                        *cc = '.';
                        rock_count+=1;
                    }
                    else if *cc == '#' {
                        self.fill_in_rocks_north(column_number, i+1, rock_count);
                        rock_count = 0;
                    }
                }
            }
        }
        self.fill_in_rocks_north(column_number,0,rock_count);
    }
    fn fill_in_rocks_north(&mut self, column: usize, row: usize, number: usize) {
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
        println!("");
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
    plane.cycle_cnt(1000000000);
    println!("Total Weight is: {}",plane.score());
    Ok(())
}