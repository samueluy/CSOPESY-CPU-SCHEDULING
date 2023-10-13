# runner file

# Import the necessary modules
import algorithm_functions as af
import utils as ut

# Initialize an empty list to store process objects
processes = []

# Get user input for scheduling algorithm, number of processes, and process details
scheduling_algorithm, number_of_processes, time_quantum, processes = ut.get_user_input()

# Print the selected scheduling algorithm for verification
print(scheduling_algorithm)

# Run the selected scheduling algorithm based on user input
if scheduling_algorithm == 0:
    processes = af.fcfs(processes)
elif scheduling_algorithm == 1:
    processes = af.sjf(processes)
elif scheduling_algorithm == 2:
    processes = af.srtf(processes)
elif scheduling_algorithm == 3:
    processes = af.rr(processes, time_quantum)
else:
    print("Invalid input")

# Display the processed output for the processes
ut.display_output(processes)

# Calculate and display the average waiting time
ut.average_waiting_time(processes)
