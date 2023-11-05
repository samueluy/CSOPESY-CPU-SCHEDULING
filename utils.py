# utility functions for the project

import process

# Display the output in the desired format
def display_output(processes):
    for current in processes:
        # Calculate total waiting time for each process
        total_waiting_time = 0
        # The initial waiting time is the time until the first start time minus the arrival time
        initial_waiting_time = current.start_times[0] - current.arrival_time
        total_waiting_time += initial_waiting_time
        print(f"{current.get_id()} start time: {current.start_times[0]} end time: {current.end_times[0]} | Waiting time: {initial_waiting_time}")
        
        # For subsequent cycles, waiting time is the time since the end of the last cycle
        for i in range(1, len(current.start_times)):
            waiting_time_since_last_cycle = current.start_times[i] - current.end_times[i-1]
            total_waiting_time += waiting_time_since_last_cycle
            print(f"{current.get_id()} start time: {current.start_times[i]} end time: {current.end_times[i]} | Waiting time: {total_waiting_time}")
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