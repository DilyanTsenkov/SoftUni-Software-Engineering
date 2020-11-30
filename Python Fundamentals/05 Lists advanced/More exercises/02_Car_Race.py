times = input().split()
times = [int(el) for el in times]

left_car_times = times[:(len(times) // 2)]
right_car_times = times[(len(times) // 2 + 1):]
right_car_times.reverse()


def time_sum(car_times, all_times):
    total_time = 0
    for time in range(len(all_times) // 2):
        if car_times[time] == 0:
            total_time -= total_time * 0.2
        else:
            total_time += car_times[time]
    return total_time


left_car_total_time = time_sum(left_car_times, times)
right_car_total_time = time_sum(right_car_times, times)

if left_car_total_time < right_car_total_time:
    print(f"The winner is left with total time: {left_car_total_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_total_time:.1f}")
