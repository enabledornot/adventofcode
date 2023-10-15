use std::fs::File;
use std::io::{BufRead, BufReader};

mod cpu;

use cpu::CPU;

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);

    let mut c = CPU::new(vec![20,60,100,140,180,220]);

    for str in read.lines() {
        c.exec(&str?);
    }
    println!("Part 1 answer: {}",c.cycle_count);

    Ok(())
}