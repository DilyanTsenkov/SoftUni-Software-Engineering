from collections import deque


def best_list_pureness(*test):
    rotations = test[1]
    numbers = deque(test[0])
    max_sum = 0
    rotation = 0
    for _ in range(rotations + 1):
        summing = 0
        for i in range(len(numbers)):
            multiplied = i * int(numbers[i])
            summing += multiplied
        if summing > max_sum:
            max_sum = summing
            current_rotation = rotation
        rotation += 1
        last_number = numbers.pop()
        numbers.appendleft(last_number)
    return f"Best pureness {max_sum} after {current_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
