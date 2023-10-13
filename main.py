# runner file

import algorithm_functions as af
import utils as ut

processes = []

scheduling_algorithm, number_of_processes, time_quantum, processes = ut.get_user_input()

print(scheduling_algorithm)
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

ut.display_output(processes)
ut.average_waiting_time(processes)