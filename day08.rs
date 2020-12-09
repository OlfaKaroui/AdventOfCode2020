pub mod read_data;

fn main() {
    let instructions = read_data::get_data_from_file("./data/data_day08");
    let (is_infinite_loop , accumulator_part_one) = get_accumulator(&instructions).unwrap();
    let accumulator_part_two = part_two(&instructions);
    println!("accumulator 1 : {:?} is infinite loop : {:?}", accumulator_part_one, is_infinite_loop );
    println!("accumulator 2 : {:?}", accumulator_part_two);
}

fn get_accumulator(instructions: &Vec<String>) -> Option<(bool, i32)> {
    let mut executed: Vec<i32> = Vec::new();
    let mut accumulator: i32 = 0;
    let mut index: i32 = 0;
    let length = instructions.len() as i32;
    while !executed.contains(&index) && index < length {
        let instruction = &instructions[index as usize];
        let inst = &instruction[0..3];
        let nbr: Result<i32, _> = instruction[4..].parse();
        executed.push(index);
        if inst == "nop" {
            index += 1;
        }
        else if inst == "acc" {
            accumulator += nbr.unwrap();
            index += 1;
        }
        else if inst == "jmp" {
            index += nbr.unwrap();
        }        
    }
    if executed.contains(&index) {
        return Some((true, accumulator));
    }
    
    return Some((false, accumulator));
}

fn part_two(instructions: &Vec<String>) -> i32 {
    for (i, instruction) in instructions.iter().enumerate() {
        let mut modified_instructions = instructions.to_vec();
        let inst = &instruction[0..3];
        let nbr: Result<i32, _> = instruction[4..].parse();

        if inst == "nop" {
            modified_instructions[i] = format!("jmp {}", nbr.unwrap().to_string());
        } else if inst == "jmp" {
            modified_instructions[i] = format!("nop {}", nbr.unwrap().to_string());
        }
        let (is_infinite_loop , accumulator_part_two) = get_accumulator(&modified_instructions).unwrap();
        if !is_infinite_loop {
            return accumulator_part_two;
        }
    }
    return 0;
}