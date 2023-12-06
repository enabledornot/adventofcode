use std::fs::File;
use std::io::{BufRead, BufReader};

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

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut times: Vec<i64> = Vec::new();
    let mut distances: Vec<i64> = Vec::new();
    let mut cnt = 0;
    for str in read.lines() {
        let line = str?;
        if cnt==0 {
            times = split_to_int(&line);
        }
        else if cnt==1 {
            distances = split_to_int(&line);
        }
        cnt+=1;
    }
    let mut time_mult = 1;
    for (&time, &distance) in times.iter().zip(distances.iter()) {
        println!("time={},distance={}",time,distance);
        let sqrt_term = ((time*time - 4*distance) as f64).sqrt();
        let first_time_valid = ((time as f64 - sqrt_term)/2.0).ceil() as i64;
        let last_time_valid = ((time as f64 + sqrt_term)/2.0).floor() as i64;
        println!("first_time={},last_time={}",first_time_valid,last_time_valid);
        if last_time_valid > time {
            time_mult*=(time-first_time_valid + 1);
        }
        else {
            time_mult*=(last_time_valid-first_time_valid + 1);
        }
    }
    println!("The product of the times is {}",time_mult);
    Ok(())
}