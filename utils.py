# utility functions for the project

import process

# Display the output in the desired format
def display_output(processes):
    for current in processes:
        # Extracting multiple start and end times and converting them to strings for clean printing
        start_times_str = " ".join(map(str, current.start_times))
        end_times_str = " ".join(map(str, current.end_times))

        # Displaying all relevant information for each process
        print(f"{current.get_id()} start time: {start_times_str} end time: {end_times_str} "
              f"| Waiting time: {current.get_waiting_time()} ")

# Calculate and display the average waiting time
def average_waiting_time(processes):
    total_waiting_time = 0
    for current in processes:
        total_waiting_time += current.get_waiting_time()
    average_waiting_time = total_waiting_time / len(processes)
    
    print(f"Average waiting time: {average_waiting_time}")

# Get user input for scheduling algorithm, number of processes, and process details
def get_user_input():
    processes = []
    scheduling_algorithm, number_of_processes, time_quantum = map(int, input().split())
    # Set time_quantum = 1 if scheduling_algorithm is not RR (3)
    if scheduling_algorithm != 3:
        time_quantum = 1
    
    for inst in range(number_of_processes):
        id, arrival_time, burst_time = map(int, input().split())
        processes.append(process.Process(id=id, arrival_time=arrival_time, burst_time=burst_time))
    return scheduling_algorithm, number_of_processes, time_quantum, processes
