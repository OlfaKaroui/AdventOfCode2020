use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};


fn main() {
    let mut rows = get_data_from_file("./data_day03");
    let one_down_slice: &mut [String] = &mut rows[1..];
    // Right 7 Down 1
    get_number_of_trees(one_down_slice, 3, 1);
    // Right 7 Down 1
    get_number_of_trees(one_down_slice, 7, 1);

    // Right 1 Down 2 
    let two_down_slice: &mut [String] = &mut rows[2..];
    get_number_of_trees(two_down_slice, 1, 2);
}


fn get_number_of_trees(rows: &mut [String], right_step: usize, down_step: usize) -> u32 {
    let mut number_trees = 0;
    let mut column_index = right_step as usize;
    for row in rows.iter().step_by(down_step) {
        let column_character = row.chars().nth(column_index);
        if column_character == Some('#') {
            number_trees += 1;
        }
        column_index += right_step;
        if column_index >= row.len() {
            column_index = column_index - row.len();
            }
    }
    return number_trees
    
}


fn get_data_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("File doesn't exist");
    let buffer = BufReader::new(file);
    buffer.lines()
        .map(|l| l.expect("Error parsing row"))
        .collect()
}
