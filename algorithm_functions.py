import process

# First-Come-First-Serve (FCFS)
def fcfs(process):
    # sort by arrival time
    for inst in range(len(process)):
        current = process[inst]
        if current.arrival_time > current.arrival_time:
            temp = current.arrival_time
            current.arrival_time = current.arrival_time
            current.arrival_time = temp
    # set waiting time
    for inst in range(len(process)):
        current = process[inst]
        if inst == 0:
            current.waiting_time = 0
        else:
            current.waiting_time = process[inst - 1].waiting_time + process[inst - 1].burst_time
    # set end time
    for inst in range(len(process)):
        current = process[inst]
        current.end_time = current.arrival_time + current.burst_time + current.waiting_time
    return process

# Shortest-Job First (SJF)

# Shortest-Remaining-Time-First (SRTF)

# Round-Robin (RR)