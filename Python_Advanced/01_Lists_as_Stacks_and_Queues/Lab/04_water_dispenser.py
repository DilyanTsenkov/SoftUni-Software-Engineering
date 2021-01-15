from collections import deque

water = int(input())

COMMAND_ONE = "Start"
COMMAND_TWO = "End"
COMMAND_THREE = "refill"
queue = deque()

while True:
    name = input()
    if name == COMMAND_ONE:
        break
    queue.append(name)

while True:
    liters_refill = input()
    if liters_refill == COMMAND_TWO:
        print(f"{water} liters left")
        break
    elif liters_refill.startswith(COMMAND_THREE):
        liters_refill = liters_refill.split()
        water += int(liters_refill[1])
    else:
        if water >= int(liters_refill):
            water -= int(liters_refill)
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
