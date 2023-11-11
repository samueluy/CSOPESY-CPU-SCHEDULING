#!/bin/bash

# Directory containing your input files
input_directory="inputs"

# Directory where you want to save the output files
output_directory="outputs"

# Loop through each input file in the input directory
for input_file in "$input_directory"/input*.txt; do
    # Extract the file number from the input file name
    file_number=$(echo "$input_file" | grep -o -E '[0-9]+')

    # Define the corresponding output file path
    output_file="$output_directory/output$file_number.txt"

    # Run the main.py script with the input file and redirect output to the output file
    python main.py < "$input_file" > "$output_file"

    echo "Processed $input_file -> $output_file"
done
