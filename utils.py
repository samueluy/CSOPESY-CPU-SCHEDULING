# utility functions for the project

import process

def display_output(process):
    sort_by_name(process)
    for inst in len(process):
        current = process[inst]
        print(current.id, + " start time: ", current.arrival_time, " end time: ", current.end_time, " | Waiting time: ", current.waiting_time, " | Turnaround time: ")
        print(average_waiting_time(process))

def sort_by_name(process):
    for inst in len(process):
        current = process[inst]
        if current.id > current.id:
            temp = current.id
            current.id = current.id
            current.id = temp
    return process

def average_waiting_time(process):
    total = 0
    for inst in len(process):
        current = process[inst]
        total += current.waiting_time
    return total / len(process)

def get_user_input():
    processes = []
    scheduling_algorithm, number_of_processes, time_quantum = map(int, input().split())
    # set time_quantum = 1 if scheduling_algorithm is not RR (3)
    if scheduling_algorithm != 3:
        time_quantum = 1
    
    for inst in range(number_of_processes):
        id, arrival_time, burst_time = map(int, input().split())
        processes.append(process.Process(id, arrival_time, burst_time))
    return scheduling_algorithm, number_of_processes, time_quantum, process