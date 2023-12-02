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

fn calculate_power(game_rounds : Vec<Round>) -> i32 {
    let mut max_red = 0;
    let mut max_green = 0;
    let mut max_blue = 0;
    for round in game_rounds {
        if round.red_count > max_red {
            max_red = round.red_count;
        }
        if round.green_count > max_green {
            max_green = round.green_count;
        }
        if round.blue_count > max_blue {
            max_blue = round.blue_count;
        }
    }
    return max_red * max_green * max_blue;
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
        count+=calculate_power(game.game_rounds);
    }
    println!("Sum of round powers is: {}",count);
    Ok(())
}