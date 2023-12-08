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

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut directions = String::new();
    let mut cnt = 0;
    let mut direction_mapping = BTreeMap::new();
    for str in read.lines() {
        let line = str?;
        if cnt==0 {
            directions = line;
        }
        else if cnt>=2 {
            let parsed = read_code(&line);
            direction_mapping.insert(parsed[0],[parsed[1],parsed[2]]);
        }
        cnt+=1;
    }
    let mut current_position: [char; 3] = ['A','A','A'];
    let mut count = 0;
    let mut broken = true;
    'outer: loop {
        for ch in directions.chars() {
            println!("{:?}",current_position);
            if current_position==['Z','Z','Z'] {
                println!("REACHED ZZZ");
                break 'outer;
            }
            current_position = lookup_direction(&direction_mapping, current_position, ch);
            count+=1;
        }
    }
    println!("Travel Count: {}",count);
    Ok(())
}