use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut sum = 0;
    for str in read.lines() {
        let line = str;
        let mut first: i32 = -1;
        let mut last: i32 = -1;
        for char in line?.chars() {
            if let Some(digit) = char.to_digit(10) {
                if first==-1{
                    first = digit as i32;
                }
                last = digit as i32;
            }
        }
        sum+=10*first;
        sum+=last;
    }
    println!("The answer to Part 1 is: {}",sum);
    Ok(())
}