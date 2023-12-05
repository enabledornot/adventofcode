use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;


struct Card {
    card_number: i32,
    winning_numbers: HashSet<i32>,
    card_numbers: HashSet<i32>
}

fn split_to_int(line: &str) -> HashSet<i32> {
    let split_string: Vec<&str> = line.split(" ").collect();
    let mut split_num: HashSet<i32> = HashSet::new();
    for number in split_string {
        if let Ok(number_int) = number.parse::<i32>() {
            split_num.insert(number_int);
            // println!("{}",number_int);
        }
    }
    return split_num;
}

impl Card {
    fn new(card_line: &str) -> Card {
        let label_split: Vec<&str> = card_line.split(":").collect();
        let mut card_num = 0;
        if let Ok(cn) = label_split[0].split(' ').collect::<Vec<_>>()[1].parse::<i32>() {
            card_num = cn;
        }
        let card_split: Vec<_> = label_split[1].split("|").collect();
        Card {
            card_number: card_num,
            winning_numbers: split_to_int(card_split[0]),
            card_numbers: split_to_int(card_split[1])
        }
    }
    fn score(self) -> i32 {
        let powcount = self.winning_numbers.intersection(&self.card_numbers).count();
        println!("Powcount: {}",powcount);
        if powcount==0 {
            return 0;
        }
        let mut pow: i32 = 1;
        for _ in 1..powcount {
            pow*=2;
        }
        println!("Power: {}",pow);
        return pow;
    }
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut card_list: Vec<Card> = Vec::new();
    for str in read.lines() {
        let line = str?;
        let current_card = Card::new(&line);
        card_list.push(current_card);
    }
    let mut sum = 0;
    for ccard in card_list {
        sum+=ccard.score();
    }
    println!("The Sum of Card Scores is : {}",sum);
    Ok(())
}