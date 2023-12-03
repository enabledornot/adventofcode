use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

struct Map {
    array: Vec<Vec<char>>
}

impl Map {
    fn new(array_map: Vec<Vec<char>>) -> Map{
        Map {
            array: array_map
        }
    }
    fn get(&self, x_pos: i32, y_pos: i32) -> char {
        if y_pos < 0 || x_pos < 0 {
            return '.';
        }
        if y_pos >= self.array.len() as i32 {
            return '.';
        }
        if x_pos >= self.array[y_pos as usize].len() as i32 {
            return '.';
        }
        return self.array[y_pos as usize][x_pos as usize];
    }
}

fn find_first(map: &Map, mut x_pos: i32, y_pos: i32) -> [i32;2] {
    while map.get(x_pos,y_pos).is_digit(10) {
        x_pos-=1;
    }
    return [x_pos+1,y_pos];
}

fn find_number(map: &Map, x_pos: i32, y_pos: i32) -> HashSet<[i32;2]> {
    let directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];
    let mut rslt: HashSet<[i32 ; 2]> = HashSet::new();
    for &direction in &directions {
        let try_x: i32 = x_pos + direction[0];
        let try_y: i32 = y_pos + direction[1];
        if map.get(x_pos + direction[0], y_pos + direction[1]).is_digit(10) {
            let starting_cords: [i32 ; 2] = find_first(map,try_x,try_y);
            if !rslt.contains(&starting_cords) {
                rslt.insert(starting_cords);
            }
        }
    }
    return rslt;
}

fn read_number(map: &Map, mut starting: [i32;2]) -> i32{
    let mut number : i32 = 0;
    while let Some(digit) = map.get(starting[0],starting[1]).to_digit(10) {
        number*=10;
        number+=digit as i32;
        starting[0]+=1;
    }
    return number
}

fn calculate_gear_ratio(map: &Map, start_cords: HashSet<[i32;2]>) -> i32{
    let mut prod = 1;
    for cord in start_cords.iter().collect::<Vec<_>>() {
        prod*=read_number(map,*cord);
    }
    return prod;
}

fn find_gear_sum(map: &Map) -> i32 {
    let mut sum = 0;
    for (y , line) in map.array.iter().enumerate() {
        for (x , c) in line.iter().enumerate() {
            if *c == '*' {
                let starting_positions = find_number(map,x as i32,y as i32);
                if starting_positions.len() == 2 {
                    sum+=calculate_gear_ratio(map,starting_positions);
                }
            }
        }
    }
    return sum
}

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut array_map: Vec<Vec<char>> = Vec::new();
    for str in read.lines() {
        let line = str?;
        array_map.push(line.chars().collect());
    }
    let map = Map::new(array_map);
    let gear_sum = find_gear_sum(&map);
    println!("The Sum of the Gear Ratios  is: {}",gear_sum);
    Ok(())
}