use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use std::collections::BTreeMap;

struct Spring_Line {
    line: String,
    lengths: Vec<i32>
}

fn read_spring_line(line: &str) -> Spring_Line {
    let mut splitt = line.split(" ");
    let first_line = if let Some(first) = splitt.next() {
        first.to_string()
    }
    else {
        String::new()
    };
    let lengthz = if let Some(last) = splitt.next() {
        split_to_int(last)
    }
    else {
        Vec::new()
    };
    return Spring_Line {
        line: first_line,
        lengths: lengthz
    }
}

fn split_to_int(line: &str) -> Vec<i32> {
    let split_string: Vec<&str> = line.split(",").collect();
    let mut split_num: Vec<i32> = Vec::new();
    split_num.push(-1);
    for number in split_string {
        if let Ok(number_int) = number.parse::<i32>() {
            split_num.push(number_int);
        }
    }
    return split_num;
}

fn simulate_empty(row: &String, to_do: &Vec<i32>) -> i32 {
    let mut new_to_do = to_do.clone();
    let rest = (*row).clone().chars().skip(1).collect();
    if let Some(first_element) = new_to_do.first_mut() {
        if *first_element > 0 {
            return 0;
        }
        *first_element-=1;
    }
    else {
        return 0;
    }
    return choice_count(&rest,&new_to_do);
}

fn simulate_spring(row: &String, to_do: &Vec<i32>) -> i32 {
    let rest = (*row).clone().chars().skip(1).collect();
    let mut new_to_do = to_do.clone();
    if let Some(first_element) = new_to_do.first() {
        if *first_element < 0 {
            new_to_do.remove(0);
        }
    }
    if let Some(first_element) = new_to_do.first_mut() {
        if *first_element < 1 {
            return 0;
        }
        *first_element-=1;
        return choice_count(&rest,&new_to_do);
    }
    else {
        return 0;
    }
}

fn choice_count(row: &String, to_do: &Vec<i32>) -> i32 {
    // println!("Choice count called with {},{:?}",row,to_do);
    if let Some(first_char) = row.chars().next() {
        if first_char == '.' {
            return simulate_empty(&row,&to_do);
        }
        else if first_char == '#' {
            return simulate_spring(&row,&to_do);
        }
        else if first_char == '?' {
            let mut sum = 0;
            sum += simulate_empty(&row,&to_do);
            sum += simulate_spring(&row,&to_do);
            return sum;
        }
    }
    else {
        // println!("END CONDITION {}-{:?}",row,to_do);
        if let Some(first_element) = to_do.first() {
            if *first_element <= 0 && to_do.len()==1 {
                return 1;
            }
        }
    }
    return 0;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut sum = 0;
    for str in read.lines() {
        let line = str?;
        let cs = read_spring_line(&line);
        println!("{}-{:?}",cs.line,cs.lengths);
        let rslt = choice_count(&cs.line, &cs.lengths);
        println!("current: {}",rslt);
        // println!("\n\n\n");
        sum+=rslt;
        // break;
    }
    println!("The Sum of the possible moves is: {}",sum);
    Ok(())
}