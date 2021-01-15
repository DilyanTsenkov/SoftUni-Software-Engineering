from collections import deque

stations = int(input())

petrol_queue = deque()
distance_queue = deque()

for _ in range(stations):
    petrol, distance = (int(x) for x in input().split())
    petrol_queue.append(petrol)
    distance_queue.append(distance)

counter_one = 0
counter_two = 0

while counter_two != stations:
    temp_distance_queue = distance_queue.copy()
    temp_petrol_queue = petrol_queue.copy()
    my_petrol = 0
    counter_two = 0
    for _ in range(stations):
        distance_to_next = temp_distance_queue.popleft()
        fuel = temp_petrol_queue.popleft()
        if my_petrol + fuel < distance_to_next:
            counter_two = 0
            break
        else:
            my_petrol += fuel
            my_petrol -= distance_to_next
            temp_distance_queue.append(distance_to_next)
            temp_petrol_queue.append(fuel)
            counter_two += 1
    counter_one += 1
    distance_queue.append(distance_queue.popleft())
    petrol_queue.append(petrol_queue.popleft())

start_station = counter_one - 1
print(start_station)
