use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

pub fn get_data_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("File doesn't exist");
    let buffer = BufReader::new(file);
    buffer.lines()
        .map(|l| l.expect("Error parsing row"))
        .collect()
}