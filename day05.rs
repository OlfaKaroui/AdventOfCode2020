pub mod read_data;

fn main() {
    let inputs = read_data::get_data_from_file("./data/data_day05");

    let mut rows: Vec<u32> = (0..128).collect();
    let mut seats: Vec<u32> = (0..8).collect();
    let mut seat_ids: Vec<u32> = Vec::new();

    for input in inputs {
        let instructions: Vec<char> = input.chars().collect();
        let row = binary_search(&mut rows, &instructions[0..7]);
        let seat = binary_search(&mut seats, &instructions[7..]);
        let seat_id = row.unwrap() * 8 + seat.unwrap();
        seat_ids.push(seat_id);
    }
    // getting max id
    let max = seat_ids.iter().max().unwrap() as &u32;
    println!("Max ID: {}",max);
    
    // sort seat IDs vector
    seat_ids.sort();
    let my_id = search_missing(seat_ids);
    println!("My ID: {}",my_id.unwrap());
}

fn binary_search(array: &mut Vec<u32>, instructions: &[char]) -> Option<u32> {
    let mut min: u32 = 0;
    let mut max: u32 = array.len() as u32 - 1;
    let instructions_length = instructions.len();
    for (index, instruction) in instructions.iter().enumerate() {
        let middle = ((max - min) / 2) + min;
        if index == instructions_length - 1 {
            if is_upper_half(instruction) {
                return Some(middle + 1);
            }
            else if is_lower_half(instruction) {
                return Some(middle);
            }
        }
        else {
            if is_upper_half(instruction) {
                min = middle + 1;
            }
            else if is_lower_half(instruction) {
                max = middle;
            }
        }
    }
    None
}

// function needs a sorted vector to work
fn search_missing(array: Vec<u32>) -> Option<u32> {
    let min = array.iter().min().unwrap() as &u32;
    for (index, id) in array.iter().enumerate() {
        let ind = index as u32;
        // subtract min ID and see if current index matches new value 
        // if it doesn't that means that my id is supposed to be here but it isn't 🤷‍♀️
        if ind != *id - min {
            return Some(ind + min);
        }
    }
    None
}

fn is_lower_half(rule: &char) -> bool {
    return *rule == 'F' || *rule == 'L'
}

fn is_upper_half(rule: &char) -> bool {
    return *rule == 'R' || *rule == 'B'
}


