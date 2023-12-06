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
    maps: BTreeMap<i64, Map>
}

impl Mapping {
    fn new() -> Mapping{
        Mapping {
            maps: BTreeMap::new()
        }
    }
    fn add(&mut self,line: &str) {
        let map_data = split_to_int(line);
        if let [dest,sorc,range] = map_data.as_slice() {
            let new_map = Map {
                dest_start: *dest,
                sorc_start: *sorc,
                range_length: *range,
                delta: (*dest)-(*sorc),
                sorc_end: (*sorc)+(*range)
            };
            println!("{} {} {} {}",new_map.dest_start,new_map.sorc_start,new_map.range_length,new_map.delta);
            self.maps.insert(*sorc, new_map);
        }
        else {
            println!("Slicing Error");
        }
    }
    fn lookup(&self, key: i64) -> i64 {
        if let Some((_, map)) = self.maps.range(..key).next_back() {
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
    fn lookup_range(&self, key: [i64; 2]) -> Vec<[i64; 2]> {
        let mut result_ranges: Vec<i64> = Vec::new();
        let mut single_range: Vec<[i64; 2]> = Vec::new();
        let mut start_map;
        if let Some((_, map)) = self.maps.range(..=key[0]).next_back() {
            start_map = Some(map);
            
        } 
        else {
            start_map = None;
        }
        let mut start_bound = 0;
        if let Some(map) = start_map {
            if key[0] <= map.sorc_end {
                result_ranges.push(key[0] + map.delta);
                if key[1] <= map.sorc_end {
                    println!("a");
                    result_ranges.push(key[1] + map.delta);
                }
                else {
                    println!("b");
                    result_ranges.push(map.sorc_end + map.delta - 1);
                    result_ranges.push(map.sorc_end);
                }
            }
            else {
                result_ranges.push(key[0]);
            }
        }
        else {
            result_ranges.push(key[0]);
            println!("f");
        }

        for (_,map) in self.maps.range(key[0]..=key[1]) {
            println!("c");
            result_ranges.push(map.sorc_start-1);
            result_ranges.push(map.dest_start);
            if key[1] <= map.sorc_end {
                println!("d");
                result_ranges.push(key[1] + map.delta);
            }
            else {
                println!("e");
                result_ranges.push(map.sorc_end + map.delta - 1);
                result_ranges.push(map.sorc_end);
            }
        }

        if result_ranges.len()%2 == 1 {
            println!("Topping off!");
            result_ranges.push(key[1]);
        }

        // println!("The magic array is {:?}",result_ranges);
        return filter_invalid_ranges(buddy_up(result_ranges));
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

fn buddy_up(single: Vec<i64>) -> Vec<[i64; 2]> {
    let mut buddied: Vec<[i64; 2]> = Vec::new();
    let mut my_single = single.clone();
    while my_single.len()!=0 {
        let new_range: [i64 ; 2] = [my_single.remove(0),my_single.remove(0)];
        buddied.push(new_range);
    }
    return buddied
}

fn find_location(mappings: &Vec<Mapping>, seed: i64) -> i64 {
    let mut cindex = seed;
    for mapping in mappings.iter() {
        cindex = mapping.lookup(cindex);
    }
    return cindex;
}

fn find_location_ranges(mappings: &Vec<Mapping>, seed: [i64; 2]) -> Vec<[i64; 2]> {
    let mut lookup_ranges: Vec<[i64; 2]> = Vec::new();
    lookup_ranges.push(seed);
    let mut count = 0;
    for mapping in mappings.iter() {
        // println!("Hello World");
        println!("{}: {:?}",count,lookup_ranges);
        let mut next_lookup_ranges: Vec<[i64; 2]> = Vec::new();
        for lookup_range in lookup_ranges.iter() {
            next_lookup_ranges.extend(mapping.lookup_range(*lookup_range));
        }
        lookup_ranges = next_lookup_ranges;
        count+=1;
    }
    println!("Final Ranges: {:?}",lookup_ranges);
    return lookup_ranges;
}

fn fix_ranges(mut ranges: Vec<[i64; 2]>) -> Vec<[i64; 2]> {
    for range in ranges.iter_mut() {
        range[1]+=range[0]-1
    }
    return ranges;
}

fn filter_invalid_ranges(input: Vec<[i64; 2]>) -> Vec<[i64; 2]> {
    input.into_iter().filter(|&range| range[1] >= range[0] && range[0]>1).collect()
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
    let seed_list_ranges: Vec<[i64; 2]> = fix_ranges(buddy_up(seed_list));
    // let mut min_seed: i64 = i64::MAX;
    let mut ranges: Vec<[i64; 2]> = Vec::new();
    for seed_range in seed_list_ranges.iter() {
        ranges.extend(find_location_ranges(&mappings, *seed_range));
    }
    println!("The ranges are: {:?}",ranges);
    let mut min = i64::MAX;
    for range in ranges.iter() {
        if range[0]<min {
            min = range[0];
        }
    }
    println!("The minimum range is {}",min);
    // println!("The ranges are: {:?}",ranges);
    Ok(())
}