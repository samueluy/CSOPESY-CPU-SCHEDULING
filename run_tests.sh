#!/bin/bash

echo "1) FCFS"
echo "2) RR"
echo "3) SJF"
echo "4) SRTF"
echo "5) ALL"
echo
read -p "Input Number: " opt

# Assign the corresponding folder names to the 'folders' array based on user selection
case $opt in
    1) folders=("FCFS") ;;
    2) folders=("RR") ;;
    3) folders=("SJF") ;;
    4) folders=("SRTF") ;;
    5) folders=("FCFS" "RR" "SJF" "SRTF") ;;
    *) echo "Invalid option. Exiting..."; exit 1 ;;
esac

input_directory="inputs"
output_directory="outputs"

# Process the input files for each selected algorithm
for folder in "${folders[@]}"; do
    echo
    echo "Processing algorithm: $folder"

    # Create the output directory for the algorithm if it doesn't exist
    mkdir -p "$output_directory/$folder"

    # Loop through each input file in the algorithm's input directory
    for input_file in "$input_directory/$folder"/input*.txt; do
        # Get the file number in the input file name to be used in the output file name
        file_number=$(echo "$input_file" | grep -o -E '[0-9]+')

        output_file="$output_directory/$folder/output$file_number.txt"

        python main.py < "$input_file" > "$output_file"

        echo "Processed $input_file -> $output_file"
    done
done

echo
echo "All input test cases processed."
