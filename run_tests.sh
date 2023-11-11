#!/bin/bash

input_directory="inputs"
output_directory="outputs"

for input_file in "$input_directory"/input*.txt; do
    # Get the file number in the input file name to be used in the ouput file name
    file_number=$(echo "$input_file" | grep -o -E '[0-9]+')

    output_file="$output_directory/output$file_number.txt"

    python main.py < "$input_file" > "$output_file"

    echo "Processed $input_file -> $output_file"
done
