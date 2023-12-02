pub struct CPU {
    pub cycle_count: i32,
    x: i32,
    clock: i32,
    print_list: Vec<i32>, 
}

impl CPU {
    pub fn new(pl: Vec<i32>) -> Self{
        CPU{
            cycle_count:0,
            x:1,
            clock:0,
            print_list:pl,
        }
    }
    pub fn exec(&mut self, inst: &str) {
        if inst.starts_with("noop") {
            self.cycle();
        }
        else {
            self.cycle();
            self.cycle();
            let number_string = &inst[5..];
            match number_string.parse::<i32>() {
                Ok(number_integer) => {
                    self.x+=number_integer;
                }
                Err(_err) => {
                    println!("Failed to parse");
                }
            }
        }
    }
    fn cycle(&mut self) {
        self.clock+=1;
        // Part 1 code
        if self.print_list.contains(&self.clock) {
            self.cycle_count+=self.x*self.clock;
        }
        // Part 2 code
        if (self.clock%40-(self.x+1)).abs() < 2 {
            print!("█");
        }
        else {
            print!(" ");
        }
        if self.clock%40 == 0 {
            println!("");
        }
    }
}