use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use std::collections::BTreeMap;

#[derive(Ord)]
#[derive(Eq)]
#[derive(PartialOrd)]
#[derive(PartialEq)]
#[derive(Clone)]
struct SpringLine {
    line: String,
    lengths: Vec<i64>
}

struct CachedSim {
    cache: BTreeMap<SpringLine, i64>
}

impl CachedSim {
    fn new() -> CachedSim {
        CachedSim {
            cache: BTreeMap::new()
        }
    }
    fn simulate_empty(&mut self, sl: &SpringLine) -> i64 {
        let mut new_to_do = sl.lengths.clone();
        let rest = (sl.line).clone().chars().skip(1).collect();
        if let Some(first_element) = new_to_do.first_mut() {
            if *first_element > 0 {
                return 0;
            }
            *first_element-=1;
        }
        else {
            return 0;
        }
        return self.choice_count(&SpringLine {
            line: rest,
            lengths: new_to_do
        });
    }
    
    fn simulate_spring(&mut self, sl: &SpringLine) -> i64 {
        let rest = (sl.line).clone().chars().skip(1).collect();
        let mut new_to_do = sl.lengths.clone();
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
            return self.choice_count(&SpringLine {
                line: rest,
                lengths: new_to_do
            });
        }
        else {
            return 0;
        }
    }
    
    fn choice_count(&mut self, sl: &SpringLine) -> i64 {
        if let Some(cache_lookup) = self.cache.get(sl) {
            return *cache_lookup;
        }
        else {
            let rslt = self.choice_count_u(sl);
            self.cache.insert(sl.clone(),rslt);
            return rslt;
        }
    }

    fn choice_count_u(&mut self, sl: &SpringLine) -> i64 {
        // println!("Choice count called with {},{:?}",row,to_do);
        if let Some(first_char) = sl.line.chars().next() {
            if first_char == '.' {
                return self.simulate_empty(&sl);
            }
            else if first_char == '#' {
                return self.simulate_spring(&sl);
            }
            else if first_char == '?' {
                let mut sum = 0;
                sum += self.simulate_empty(&sl);
                sum += self.simulate_spring(&sl);
                return sum;
            }
        }
        else {
            // println!("END CONDITION {}-{:?}",row,to_do);
            if let Some(first_element) = sl.lengths.first() {
                if *first_element <= 0 && sl.lengths.len()==1 {
                    return 1;
                }
            }
        }
        return 0;
    }
}

fn fivex_string(s: &str) -> String {
    format!("{}?{}?{}?{}?{}",s,s,s,s,s)
}

fn fivex_vector(vec: Vec<i64>) -> Vec<i64> {
    let repeated: Vec<i64> = vec.iter().cloned().cycle().take(vec.len() * 5).collect();
    repeated

}

fn read_SpringLine(line: &str) -> SpringLine {
    let mut splitt = line.split(" ");
    let first_line = if let Some(first) = splitt.next() {
        first.to_string()
    }
    else {
        String::new()
    };
    let mut lengthz = if let Some(last) = splitt.next() {
        fivex_vector(split_to_int(last))
    }
    else {
        Vec::new()
    };
    lengthz.insert(0,-1);
    return SpringLine {
        line: fivex_string(&first_line),
        lengths: lengthz
    }
}

fn split_to_int(line: &str) -> Vec<i64> {
    let split_string: Vec<&str> = line.split(",").collect();
    let mut split_num: Vec<i64> = Vec::new();
    for number in split_string {
        if let Ok(number_int) = number.parse::<i64>() {
            split_num.push(number_int);
        }
    }
    return split_num;
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input.txt")?;
    let read = BufReader::new(file);
    let mut sum = 0;
    for str in read.lines() {
        let line = str?;
        let cs = read_SpringLine(&line);
        let mut cashsim = CachedSim::new();
        // println!("{}-{:?}",cs.line,cs.lengths);
        let rslt = cashsim.choice_count(&cs);
        println!("current: {}",rslt);
        // println!("\n\n\n");
        sum+=rslt;
        // break;
    }
    println!("The Sum of the possible moves is: {}",sum);
    Ok(())
}