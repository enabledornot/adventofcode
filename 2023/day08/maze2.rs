use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use std::collections::BTreeMap;

fn read_code(line: &str) -> [[char; 3]; 3] {
    let mut split: [[char; 3]; 3] = [['0';3];3];
    let mut ctr = 0;
    for char in line.chars() {
        if char.is_alphanumeric() {
            split[ctr/3][ctr%3] = char;
            ctr+=1;
        }
    }
    return split;
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: i64, b: i64) -> i64 {
    if a == 0 || b == 0 {
        0
    } else {
        (a * b) / gcd(a, b)
    }
}

fn lookup_direction(BT: &BTreeMap<[char; 3],[[char; 3]; 2]> ,current_pos: [char; 3], direction: char) -> [char; 3] {
    if let Some(&value) = BT.get(&current_pos) {
        if direction=='R' {
            return value[1];
        }
        else {
            return value[0];
        }
    }
    println!("KEY LOOKUP ERROR");
    return ['0','0','0'];
}

fn get_trip_count(direction_mapping: &BTreeMap<[char; 3],[[char; 3]; 2]>, start_pos: [char; 3], directions: &str) -> i64 {
    let mut count = 0;
    let mut current_position = start_pos.clone();
    'outer: loop {
        for ch in directions.chars() {
            if current_position[2]=='Z' {
                break 'outer;
            }
            current_position = lookup_direction(direction_mapping, current_position, ch);
            count+=1;
        }
    }
    return count;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut directions = String::new();
    let mut cnt = 0;
    let mut direction_mapping = BTreeMap::new();
    let mut ending_in_a: Vec<[char; 3]> = Vec::new();
    for str in read.lines() {
        let line = str?;
        if cnt==0 {
            directions = line;
        }
        else if cnt>=2 {
            let parsed = read_code(&line);
            direction_mapping.insert(parsed[0],[parsed[1],parsed[2]]);
            if parsed[0][2] == 'A' {
                ending_in_a.push(parsed[0]);
            }
        }
        cnt+=1;
    }
    let mut Ztime: Vec<i64> = Vec::new();
    for a_ender in ending_in_a.iter() {
        Ztime.push(get_trip_count(&direction_mapping, *a_ender, &directions))
    }
    let mut lcmed = 1;
    while let Some(current) = Ztime.pop() {
        lcmed = lcm(lcmed,current);
    }
    println!("All nodes end in Z in: {} steps",lcmed);
    Ok(())
}