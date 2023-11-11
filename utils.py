# utility functions for the project

import sys
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
            print(f"{current.get_id()} start time: {current.start_times[i]} end time: {current.end_times[i]} | Waiting time: {waiting_time_since_last_cycle}")
def average_waiting_time(processes):
    total_waiting_time = 0
    for current in processes:
        total_waiting_time += current.get_waiting_time()
    average_waiting_time = total_waiting_time / len(processes)

    print(f"Average waiting time: {average_waiting_time:.2f}")


# Get user input for scheduling algorithm, number of processes, and process details
def get_user_input():
    processes = []
    scheduling_algorithm, number_of_processes, time_quantum = map(int, input().split())

    # Validate number of processes
    if number_of_processes < 3 or number_of_processes > 100:
        print("Invalid number of processes. Enter a value between 3 and 100.")
        sys.exit("Exiting due to invalid number of processes.")

    # Set time_quantum = 1 if scheduling_algorithm is not RR (3)
    if scheduling_algorithm != 3:
        time_quantum = 1
    else:
        # Validate time quantum only if the algorithm is Round Robin
        if time_quantum < 1 or time_quantum > 100:
            print("Invalid time quantum. Enter a value between 1 and 100.")
            sys.exit("Exiting due to invalid time quantum.")
    
    for inst in range(number_of_processes):
        id, arrival_time, burst_time = map(int, input().split())
        processes.append(process.Process(id=id, arrival_time=arrival_time, burst_time=burst_time))
    return scheduling_algorithm, number_of_processes, time_quantum, processes