def cpu_use(process, bt, tq, current_time):
    if bt >= tq:
        bt -= tq
        current_time += tq
    elif bt > 0 and bt < tq:
        current_time += bt
        bt = 0

    return bt, current_time

def wt(W):
    total_wt = sum(W)
    return total_wt / len(W)

def tat(T):
    total_tt = sum(T)
    return total_tt / len(T)

Processes = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 5},
    {"pid": "P2", "arrival_time": 1, "burst_time": 3},
    {"pid": "P3", "arrival_time": 2, "burst_time": 1}
]
time_quantum = 2

execution_lst = []
waiting_times = []
turnaround_times = []

remaining_burst_times = {process['pid']: process['burst_time'] for process in Processes}
completion_times = {process['pid']: None for process in Processes}
start_times = {process['pid']: None for process in Processes}
arrival_times = {process['pid']: process['arrival_time'] for process in Processes}

current_time = 0
completed_processes = 0
process_queue = []

for process in Processes:
   process_queue.append(process)

while completed_processes < len(Processes):
    if process_queue:
        process = process_queue.pop(0)
        pid = process['pid']
        arrival_time = process['arrival_time']
        if arrival_time <= current_time:
            bt = remaining_burst_times[pid]

            if bt > 0:
                if start_times[pid] is None:
                    start_times[pid] = current_time

                bt, current_time = cpu_use(process, bt, time_quantum, current_time)

                if bt == 0:
                    completion_times[pid] = current_time
                    remaining_burst_times[pid] = 0
                    completed_processes += 1
                else:
                    remaining_burst_times[pid] = bt

                if remaining_burst_times[pid] > 0:
                    process_queue.append(process)
                execution_lst.append(process['pid'])

for process in Processes:
    pid = process['pid']
    arrival_time = process['arrival_time']
    burst_time = process['burst_time']

    turnaround_time = completion_times[pid] - arrival_time
    turnaround_times.append(turnaround_time)

    waiting_time = turnaround_time - burst_time
    waiting_times.append(waiting_time)

a_waiting_t = wt(waiting_times)
a_turnaround_t = tat(turnaround_times)

execution_seq = " → ".join(execution_lst)
print(f"Execution Sequence: {execution_seq}")
print(f"Average Waiting Time: {a_waiting_t:.2f}")
print(f"Average Turnaround Time: {a_turnaround_t:.2f}")
