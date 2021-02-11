tasks = [int(el) for el in input().split(", ")]
task_index_interested = int(input())

tasks_time = 0
while True:
    task_max_time = max(tasks)
    task_min_time = min(tasks)
    task_to_do_index = tasks.index(task_min_time)
    tasks_time += tasks[task_to_do_index]
    tasks[task_to_do_index] = task_max_time + 1
    if task_to_do_index == task_index_interested:
        break
print(tasks_time)