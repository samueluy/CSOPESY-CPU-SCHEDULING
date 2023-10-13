# utility functions for the project

import process

def display_output(processes):
    for inst in range(len(processes)):
        current = processes[inst]
        print(f"{current.get_id()} start time: {current.get_start_time()} end time: {current.get_end_time()} | Waiting time: {current.get_waiting_time()}")
        
def average_waiting_time(processes):
    total = 0
    for current in processes:
        total += current.waiting_time
    return total / len(processes)

def get_user_input():
    processes = []
    scheduling_algorithm, number_of_processes, time_quantum = map(int, input().split())
    # set time_quantum = 1 if scheduling_algorithm is not RR (3)
    if scheduling_algorithm != 3:
        time_quantum = 1
    
    for inst in range(number_of_processes):
        id, arrival_time, burst_time = map(int, input().split())
        processes.append(process.Process(id=id, arrival_time=arrival_time, burst_time=burst_time))
    return scheduling_algorithm, number_of_processes, time_quantum, processes