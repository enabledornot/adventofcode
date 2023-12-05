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
        return powcount as i32;
    }
}

fn count_cards(card_list: Vec<Card>) -> i32 {
    let mut future_multiply: [i32; 10] = [1; 10];
    future_multiply[0] = 1;
    let mut current_index = 0;
    let mut card_count = 0;
    for card in card_list {
        println!("{:?}",future_multiply);
        let multiply_count = future_multiply[current_index];
        future_multiply[current_index] = 1;
        current_index = (current_index+1)%10;
        card_count+=multiply_count;
        let current_score = card.score();
        for i in 0..current_score {
            future_multiply[(current_index+i as usize)%10]+=multiply_count;
        }
    }
    return card_count;
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
    println!("The card count is : {}",count_cards(card_list));
    Ok(())
}