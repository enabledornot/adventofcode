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

fn remove_spaces_and_combine(line: &str) -> i64 {
    if let Some(post_colon) = line.split(":").nth(1) {
        if let Ok(parsed) = post_colon.replace(" ","").parse::<i64>() {
            println!("parsed-{}",parsed);
            return parsed;
        }
    }
    println!("Parsing error!");
    return 0;
}

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut time = 0;
    let mut distance = 0;
    let mut cnt = 0;
    for str in read.lines() {
        let line = str?;
        if cnt==0 {
            time = remove_spaces_and_combine(&line);
        }
        else if cnt==1 {
            distance = remove_spaces_and_combine(&line);
        }
        cnt+=1;
    }
    println!("time={},distance={}",time,distance);
    let sqrt_term = ((time*time - 4*distance) as f64).sqrt();
    let first_time_valid = ((time as f64 - sqrt_term)/2.0).ceil() as i64;
    let last_time_valid = ((time as f64 + sqrt_term)/2.0).floor() as i64;
    println!("first_time={},last_time={}",first_time_valid,last_time_valid);
    if last_time_valid > time {
        time = (time-first_time_valid + 1);
    }
    else {
        time = (last_time_valid-first_time_valid + 1);
    }
    println!("The product of the times is {}",time);
    Ok(())
}