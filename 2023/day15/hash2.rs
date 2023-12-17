use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashSet;
// use std::collections::BTreeMap;
use std::cmp::min;

struct Instruction {
    label: String,
    focal_length: i32
}

impl Instruction {
    fn new(line: &String) -> Instruction{
        let split: Vec<_> = line.split('=').collect();
        if split.len()==2 {
            if let Some(lb) = split.get(0) {
                if let Some(code) = split.get(1) {
                    if let Ok(number) = code.parse::<i32>() {
                        return Instruction {
                            label: lb.to_string(),
                            focal_length: number
                        }
                    }
                }
            }
        }
        if let Some(beginning) = line.get(..line.len()-1) {
            return Instruction {
                label: beginning.to_string(),
                focal_length: 0
            }
        }
        println!("PARSE ERROR");
        return Instruction {
            label: "".to_string(),
            focal_length: 0
        }
    }
    fn get_hash(&self) -> i32 {
        return hash_me(&self.label);
    }
    fn copy(self) -> Instruction {
        Instruction {
            label: self.label.clone(),
            focal_length: self.focal_length
        }
    }
}

struct Boxes {
    boxa: Vec<Vec<Instruction>>
}

impl Boxes {
    fn new() -> Boxes {
        let mut boxv: Vec<Vec<Instruction>> = Vec::new();
        for i in 0..256 {
            boxv.push(Vec::new());
        }
        Boxes {
            boxa: boxv
        }
    }
    fn import_instruction(&mut self, inst: Instruction) {
        let box_number = inst.get_hash() as usize;
        if let Some(boxo) = self.boxa.get_mut(box_number) {
            Boxes::put_into_box(boxo,inst);
        }
    }
    fn put_into_box(boxo: &mut Vec<Instruction>, inst: Instruction) {
        if inst.focal_length == 0 {
            boxo.retain(|x| x.label != inst.label);
        }
        else {
            for lense in boxo.iter_mut() {
                if lense.label == inst.label {
                    lense.focal_length = inst.focal_length;
                    return;
                }
            }
            boxo.push(inst);
        }
    }
    fn get_focus_power(&self) -> i32 {
        let mut total = 0;
        for (i,boxo) in self.boxa.iter().enumerate() {
            total += (i as i32 + 1) * Boxes::get_box_power(boxo);
        }
        return total;
    }
    fn get_box_power(boxo: &Vec<Instruction>) -> i32 {
        let mut total = 0;
        for (i,inst) in boxo.iter().enumerate() {
            total += (i as i32 + 1) * inst.focal_length;
        }
        return total;
    }
}

fn hash_me(input: &String) -> i32 {
    let mut val = 0;
    for c in input.chars() {
        val += c as i32;
        val = val * 17;
        val = val % 256;
    }
    return val;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut to_hash: Vec<String> = Vec::new();
    for str in read.lines() {
        let line = str?;
        to_hash = line.split(",").map(String::from).collect();
    }
    let mut hash_sum = 0;
    // let mut i_list: Vec<Instruction> = Vec::new();
    let mut b: Boxes = Boxes::new();
    for hash in to_hash.iter() {
        b.import_instruction(Instruction::new(hash));
    }
    println!("The Focal Power Sum is: {}",b.get_focus_power());
    Ok(())
}