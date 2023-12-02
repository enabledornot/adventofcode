use std::fs::File;
use std::io::{BufRead, BufReader};

struct Game {
    game_number : i32,
    game_rounds : Vec<Round>
}

struct Round {
    red_count : i32,
    green_count : i32,
    blue_count : i32
}

fn decode_string(line : &str) -> Game{
    let tag_split: Vec<&str> = line.split(":").collect();
    let mut gm = Game{game_number: 0, game_rounds: Vec::new()};
    if let Ok(gn) = tag_split[0].split(' ').collect::<Vec<_>>()[1].parse::<i32>() {
        gm.game_number = gn;
    }
    else {
        println!("Error occored when parsing number!");
    }
    for round_current in tag_split[1].split(';').collect::<Vec<&str>>() {
        let mut tr = Round{red_count: 0, green_count: 0, blue_count: 0};
        for color_current in round_current.split(',').collect::<Vec<&str>>() {
            let color_current_split: Vec<_> = color_current.split(' ').collect();
            // println!("red value: {}",color_current_split[1]);
            if let Ok(color_current_count) = color_current_split[1].parse::<i32>() {
                if color_current_split[2] == "red" {
                    tr.red_count = color_current_count;
                }
                else if color_current_split[2] == "green" {
                    tr.green_count = color_current_count;
                }
                else if color_current_split[2] == "blue" {
                    tr.blue_count = color_current_count;
                }
                else {
                    println!("Something impossible has happeend");
                }
            }
        }
        gm.game_rounds.push(tr);
    }

    return gm;
}

fn check_round(round : Round) -> bool {
    if round.red_count > 12 {
        return false;
    }
    else if round.green_count > 13 {
        return false;
    }
    else if round.blue_count > 14 {
        return false;
    }
    return true;
}

fn main() -> Result<(), std::io::Error>{
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut games: Vec<Game> = Vec::new();
    for str in read.lines() {
        let line = str?;
        let current_game = decode_string(&line);
        println!("{}",current_game.game_number);
        games.push(current_game);
    }
    let mut count = 0;
    for game in games{
        let mut perfect = true;
        for round in game.game_rounds {
            if check_round(round) {
                println!("Current Checked Round Number: {}",game.game_number);
            }
            else {
                println!("Failed Check!");
                perfect = false;
                break;
            }
        }
        if perfect {
            count += game.game_number;
        }
    }
    println!("Sum of Impossible Game IDs: {}",count);
    Ok(())
}