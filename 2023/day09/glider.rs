use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use std::collections::BTreeMap;

fn split_to_int(line: &str) -> Vec<i64> {
    let split_string: Vec<&str> = line.split(" ").collect();
    let mut split_num: Vec<i64> = Vec::new();
    for number in split_string {
        if let Ok(number_int) = number.parse::<i64>() {
            split_num.push(number_int);
        }
    }
    return split_num;
}

fn is_all_equal(possible_vec: &Vec<i64>) -> bool {
    return possible_vec.iter().all(|&x| x == 0);
}

fn gen_new_vec(last_vec: &Vec<i64>) -> Vec<i64> {
    let mut rslt: Vec<i64> = Vec::new();
    let mut offset = 0;
    while let (Some(a), Some(b)) = (last_vec.get(offset), last_vec.get(offset + 1))  {
        rslt.push(b-a);
        offset+=1;
    }
    return rslt;
}

fn extrapolate_value(div_line: Vec<i64>) -> i64 {
    let mut vec_list: Vec<Vec<i64>> = Vec::new();
    let mut last_vec = div_line.clone();
    vec_list.push(div_line);
    while !is_all_equal(&last_vec) {
        last_vec = gen_new_vec(&last_vec);
        vec_list.push(last_vec.clone());


    }
    let mut last = 0;
    for vector in vec_list.iter().rev() {
        println!("{:?}",vector);
        if let Some(&l) = vector.last() {
            last+=l;
        }
    }
    return last;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut sum_extrapol = 0;
    for str in read.lines() {
        let line = str?;
        let mut div_line: Vec<i64> = split_to_int(&line);
        sum_extrapol+=extrapolate_value(div_line);
    }
    println!("The sum of the extrapol values is: {}",sum_extrapol);
    Ok(())
}