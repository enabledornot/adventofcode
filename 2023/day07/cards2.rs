use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

struct Hand {
    cards_in_hand: [char; 5],
    score: i64
}

impl Hand {
    fn new(card_line: &str) -> Hand {
        let card_line_split: Vec<&str> = card_line.split(" ").collect();
        let mut new_hand = Hand {
            cards_in_hand: [' '; 5],
            score: 0
        };
        if let Some(card_line_in_hand) = card_line_split.get(0) {
            for (index,charecter) in card_line_in_hand.chars().enumerate() {
                new_hand.cards_in_hand[index] = charecter;
            }
        }
        if let Ok(card_number_parsed) = card_line_split[1].parse::<i64>() {
            new_hand.score = card_number_parsed;
        }
        return new_hand;
    }
    fn get_iscore(&self) -> i64 {
        let mut iscore: i64 = 0;
        for i in 0..=4 {
            for ii in 0..=4 {
                if self.cards_in_hand[i]==self.cards_in_hand[ii] {
                    iscore+=1;
                }
            }
        }
        return iscore;
    }
    fn get_iscore_joker(&self) -> i64 {
        let mut iscore: i64 = 0;
        let mut ary_score: [i64; 13] = [0; 13];
        for i in 0..=4 {
            for ii in 0..=4 {
                if self.cards_in_hand[i]==self.cards_in_hand[ii] {
                    iscore+=1;
                }
                else if self.cards_in_hand[ii]=='J' {
                    ary_score[char_to_point(self.cards_in_hand[i]) as usize]+=1;
                }
            }
        }
        if let Some(max) = ary_score.iter().max() {
            return iscore + 2*max;
        }
        return -1;
    }
    fn compare_to(&self, other: &Hand) -> std::cmp::Ordering {
        let iscore_me_j = self.get_iscore_joker();
        let iscore_other_j = other.get_iscore_joker();
        if iscore_me_j!=iscore_other_j {
            return iscore_me_j.cmp(&iscore_other_j);
        }
        // let iscore_me = self.get_iscore();
        // let iscore_other = other.get_iscore();
        // if iscore_me!=iscore_other {
        //     return iscore_me.cmp(&iscore_other);
        // }
        for (me,em) in self.cards_in_hand.iter().zip(other.cards_in_hand) {
            let point_me = char_to_point(*me);
            let point_em = char_to_point(em);
            if point_me!=point_em {
                return point_me.cmp(&point_em)
            }
        }
        println!("EQUAL!");
        return std::cmp::Ordering::Equal;
    }
}

fn char_to_point(ch: char) -> i64 {
    match ch {
        'A' => 12,
        'K' => 11,
        'Q' => 10,
        'T' => 9,
        '9' => 8,
        '8' => 7,
        '7' => 6,
        '6' => 5,
        '5' => 4,
        '4' => 3,
        '3' => 2,
        '2' => 1,
        'J' => 0,
        _ => -1
    }
}

fn split_to_int(line: &str) -> HashSet<i64> {
    let split_string: Vec<&str> = line.split(" ").collect();
    let mut split_num: HashSet<i64> = HashSet::new();
    for number in split_string {
        if let Ok(number_int) = number.parse::<i64>() {
            split_num.insert(number_int);
        }
    }
    return split_num;
}

fn get_total_winnings(card_list: &Vec<Hand>) -> i64 {
    let mut score: i64 = 0;
    for (index,cards) in (&card_list).iter().enumerate() {
        score+= (index as i64 + 1) * cards.score;
    }
    return score;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut card_list: Vec<Hand> = Vec::new();
    for str in read.lines() {
        let line = str?;
        let current_card = Hand::new(&line);
        card_list.push(current_card);
    }
    card_list.sort_by(|a, b| a.compare_to(b));
    println!("Total Winnings: {}",get_total_winnings(&card_list));
    Ok(())
}