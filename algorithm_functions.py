import process

def fcfs(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.get_arrival_time())

    # Initialize waiting time and end time for the first process
    processes[0].set_waiting_time(0)
    processes[0].set_end_time(processes[0].get_arrival_time() + processes[0].get_burst_time())

    # Calculate waiting time and end time for the remaining processes
    for i in range(1, len(processes)):
        processes[i].set_start_time(max(processes[i - 1].get_end_time(), processes[i].get_arrival_time()))
        processes[i].set_waiting_time(
            max(0, processes[i - 1].get_end_time() - processes[i].get_arrival_time())
        )
        processes[i].set_end_time(processes[i].get_arrival_time() + processes[i].get_waiting_time() + processes[i].get_burst_time())

    return processes


# Shortest-Job First (SJF)

# Shortest-Remaining-Time-First (SRTF)

# Round-Robin (RR)
def rr(processes, time_quantum):
    processes.sort(key=lambda x: x.get_arrival_time())
    current_time = processes[0].get_arrival_time()
    ready_queue = [processes[0]]
    remaining_time = {p.get_id(): p.get_burst_time() for p in processes}
    has_started = {p.get_id(): False for p in processes}

    while any(val > 0 for val in remaining_time.values()):
        process_to_execute = ready_queue[0] if ready_queue else None

        # If the process queue is empty, move time to the next process's arrival
        if process_to_execute is None:
            current_time = min(p.get_arrival_time() for p in processes if not has_started[p.get_id()])
            process_to_execute = [p for p in processes if p.get_arrival_time() == current_time][0]
            ready_queue.append(process_to_execute)

        if not has_started[process_to_execute.get_id()]:
            process_to_execute.set_start_time(current_time)
            has_started[process_to_execute.get_id()] = True

        # Calculating end of execution for current quantum slice
        execution_time = min(remaining_time[process_to_execute.get_id()], time_quantum)
        current_time += execution_time
        remaining_time[process_to_execute.get_id()] -= execution_time
        
        # Updating end time and other time metrics if process is finished
        if remaining_time[process_to_execute.get_id()] == 0:
            process_to_execute.set_end_time(current_time)
            process_to_execute.set_turn_around_time(current_time - process_to_execute.get_arrival_time())
            process_to_execute.set_waiting_time(process_to_execute.get_turn_around_time() - process_to_execute.get_burst_time())
        
        # Adding processes that have arrived to ready_queue and removing completed processes
        ready_queue.extend(
            p for p in processes 
            if p.get_arrival_time() <= current_time and not has_started[p.get_id()] and p not in ready_queue
        )
        ready_queue = [p for p in ready_queue if remaining_time[p.get_id()] > 0]
        
        # Ensuring cyclic execution of processes in ready_queue
        if ready_queue and process_to_execute == ready_queue[0]:
            ready_queue.append(ready_queue.pop(0))
            
    return processes