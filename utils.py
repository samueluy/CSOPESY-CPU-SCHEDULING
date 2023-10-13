# utility functions for the project

import process

# Display the output in the desired format
def display_output(processes):
    for current in processes:
        print(f"{current.get_id()} start time: {current.get_start_time()} end time: {current.get_end_time()} | Waiting time: {current.get_waiting_time()}")

# Calculate and display the average waiting time
def average_waiting_time(processes):
    total_waiting_time = 0
    for current in processes:
        total_waiting_time += current.get_waiting_time()
    average_waiting_time = total_waiting_time / len(processes)
    
    print(f"Average waiting time: {average_waiting_time:.1f}")

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
