# runner file

import algorithm_functions as af
import utils as ut

process = []

scheduling_algorithm, number_of_processes, time_quantum, process = ut.get_user_input()

if scheduling_algorithm == 1:
    process = af.fcfs(process)
elif scheduling_algorithm == 2:
    process = af.sjf(process)
elif scheduling_algorithm == 3:
    process = af.srtf(process)
elif scheduling_algorithm == 4:
    process = af.rr(process, time_quantum)
else:
    print("Invalid input")

ut.display_output(process)