use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashSet;
// use std::collections::BTreeMap;
use std::cmp::min;

fn hash_me(input: &String) -> i32 {
    let mut val = 0;
    for c in input.chars() {
        val += c as i32;
        val = val * 17;
        val = val % 256;
    }
    return val;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut to_hash: Vec<String> = Vec::new();
    for str in read.lines() {
        let line = str?;
        to_hash = line.split(",").map(String::from).collect();
    }
    let mut hash_sum = 0;
    for hash in to_hash.iter() {
        hash_sum += hash_me(hash);
    }
    println!("The Hash Sum is: {}",hash_sum);
    Ok(())
}