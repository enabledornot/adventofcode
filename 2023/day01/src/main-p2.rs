use std::fs::File;
use std::io::{BufRead, BufReader};

fn is_word(fstr: &str,sinx: usize,word: &str) -> bool{
    return fstr[sinx as usize..].starts_with(word);
}

fn to_numb_if(fstr: &str,sinx: usize) -> Option<i32> {
    if is_word(fstr,sinx,"zero") {return Some(0)}
    if is_word(fstr,sinx,"one") {return Some(1)}
    if is_word(fstr,sinx,"two") {return Some(2)}
    if is_word(fstr,sinx,"three") {return Some(3)}
    if is_word(fstr,sinx,"four") {return Some(4)}
    if is_word(fstr,sinx,"five") {return Some(5)}
    if is_word(fstr,sinx,"six") {return Some(6)}
    if is_word(fstr,sinx,"seven") {return Some(7)}
    if is_word(fstr,sinx,"eight") {return Some(8)}
    if is_word(fstr,sinx,"nine") {return Some(9)} 
    return None;
}

fn num_to_int(fstr: &str,sinx: usize,cha: char) -> Option<i32> {
    if let Some(digit) = cha.to_digit(10) {
        return Some(digit as i32);
    }
    return to_numb_if(fstr,sinx);
}

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut sum = 0;
    for str in read.lines() {
        let line = str?;
        let mut first: i32 = -1;
        let mut last: i32 = -1;
        for (num,cha) in line.chars().enumerate() {
            if let Some(digit) = num_to_int(&line,num,cha) {
                if first==-1{
                    first = digit as i32;
                }
                last = digit as i32;
            }
        }
        sum+=10*first;
        sum+=last;
    }
    println!("The answer to Part 2 is: {}",sum);
    Ok(())
}