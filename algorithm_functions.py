import process

def fcfs(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.get_arrival_time())

    # Initialize waiting time and end time for the first process
    processes[0].set_waiting_time(0)
    processes[0].set_end_time(processes[0].get_arrival_time() + processes[0].get_burst_time())

    # Calculate waiting time and end time for the remaining processes
    for i in range(1, len(processes)):
        processes[i].set_waiting_time(
            max(0, processes[i - 1].get_end_time() - processes[i].get_arrival_time())
        )
        processes[i].set_end_time(processes[i].get_arrival_time() + processes[i].get_waiting_time() + processes[i].get_burst_time())

    return processes


# Shortest-Job First (SJF)

# Shortest-Remaining-Time-First (SRTF)

# Round-Robin (RR)