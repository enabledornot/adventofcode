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
    fn find_mirror_row(&self) -> usize {
        for e in 0..self.i {
            if self.check_mirror_row(e)==1 {
                // println!("Found valid row mirror {}",e);
                return e;
            }
        }
        return 10000;
    }
    fn check_mirror_row(&self, r0: usize) -> i32 {
        let mut err = 0;
        for e in 0..=min(r0,(self.i-2).wrapping_sub(r0)) {
            err += self.compare_row(r0-e,r0+e+1);
            if err > 1 {
                return 10000;
            }
        }
        return err;
        
    }
    fn find_mirror_column(&self) -> usize {
        for e in 0..self.ii {
            if self.check_mirror_column(e)==1 {
                // println!("Found valid column mirror {}",e);
                return e;
            }
        }
        return 10000;
    }
    fn check_mirror_column(&self, c0: usize) -> i32 {
        let mut err = 0;
        for e in 0..=min(c0,(self.ii-2).wrapping_sub(c0)) {
            err += self.compare_column(c0-e,c0+e+1);
            if err > 1 {
                return 10000;
            }
        }
        return err;
        
    }
    fn compare_row(&self, r0: usize, r1: usize) -> i32 {
        // println!("comparing {}-{}",r0,r1);
        if let Some(r0s) = self.map.get(r0) {
            if let Some(r1s) = self.map.get(r1) {
                let mut err = 0;
                for (i0,i1) in r0s.iter().zip(r1s.iter()) {
                    if i0!=i1 {
                        // return false;
                        err+=1;
                    }
                }
                return err;
            }
        }
        return 10000;
    }

    fn compare_column(&self, c0: usize, c1: usize) -> i32 {
        // println!("comparing {}-{}",c0,c1);
        let mut err = 0;
        for row in self.map.iter() {
            if let Some(c0s) = row.get(c0) {
                if let Some(c1s) = row.get(c1) {
                    if c0s!=c1s {
                        // return false;
                        err+=1;
                    }
                }
                else {
                    return 10000;
                }
            }
            else {
                return 10000;
            }
        }
        return err;

    }
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut planes: Vec<Plane> = Vec::new();
    planes.push(Plane::new());
    for str in read.lines() {
        let line = str?;
        if line.len()==0 {
            planes.push(Plane::new());
            continue;
        }
        if let Some(pl) = planes.last_mut() {
            pl.add_row();
            for c in line.chars() {
                pl.add_char(c);
            }
        }
    }
    let mut sum = 0;
    for plane in planes {
        let mr = plane.find_mirror_row();
        let mc = plane.find_mirror_column();
        if mr!= 10000 {
            sum+= (mr+1)*100;
        }
        if mc!=10000 {
            sum+= mc+1;
        }
    }
    println!("The dim lines sum is: {}",sum);
    Ok(())
}