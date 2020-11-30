import math

needed_hours = int(input())
days = int(input())
employees = int(input())
working_days = days * 0.9
working_hours = working_days * 8
overtime_working = days * employees * 2
total_working_hours = math.floor(working_hours + overtime_working)
result = needed_hours - total_working_hours
if needed_hours <= total_working_hours:
    print(f'Yes!{abs(result)} hours left.')
else:
    print(f'Not enough time!{result} hours needed.')
