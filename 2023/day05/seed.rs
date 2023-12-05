use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::BTreeMap;

struct Map {
    dest_start: i64,
    sorc_start: i64,
    range_length: i64,
    delta: i64,
    sorc_end: i64
}

struct Mapping {
    map: BTreeMap<i64, Map>
}

impl Mapping {
    fn new() -> Mapping{
        Mapping {
            map: BTreeMap::new()
        }
    }
    fn add(&mut self,line: &str) {
        let map_data = split_to_int(line);
        if let [dest,sorc,range] = map_data.as_slice() {
            let new_map = Map {
                dest_start: *dest,
                sorc_start: *sorc,
                range_length: *range,
                delta: dest-sorc,
                sorc_end: sorc+range
            };
            self.map.insert(*sorc, new_map);
        }
        else {
            println!("Slicing Error");
        }
    }
    fn lookup(&self, key: i64) -> i64 {
        if let Some((_, map)) = self.map.range(..key).next_back() {
            if key < map.sorc_end {
                return key + map.delta;
            }
            else {
                return key;
            }
        }
        else {
            println!("Lookup error");
            return key;
        }
    }
}

fn split_to_int(line: &str) -> Vec<i64> {
    let split_string: Vec<&str> = line.split(" ").collect();
    let mut split_num: Vec<i64> = Vec::new();
    for number in split_string {
        if let Ok(number_int) = number.parse::<i64>() {
            split_num.push(number_int);
        }
        else {
            println!("Parse Error: {}",number);
        }
    }
    return split_num;
}

fn find_location(mappings: &Vec<Mapping>, seed: i64) -> i64 {
    let mut cindex = seed;
    for mapping in mappings.iter() {
        cindex = mapping.lookup(cindex);
    }
    return cindex;
}

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut first_line = true;
    let mut seed_list: Vec<i64> = Vec::new();
    let mut mappings: Vec<Mapping> = Vec::new();
    for str in read.lines() {
        let line = str?;
        if first_line {
            seed_list = split_to_int(&line);
            first_line = false;
        }
        else {
            if line.contains(":") {
                mappings.push(Mapping::new());
            }
            else if line.len()!=0 {
                if let Some(current_mapping) = mappings.last_mut() {
                    current_mapping.add(&line);
                }
            }
        }
    }
    let mut min_seed: i64 = i64::MAX;
    for seed in seed_list.iter() {
        let result_seed = find_location(&mappings,*seed);
        if result_seed < min_seed {
            min_seed = result_seed;
        }
    }
    println!("The smallest seed location is: {:?}",min_seed);
    Ok(())
}