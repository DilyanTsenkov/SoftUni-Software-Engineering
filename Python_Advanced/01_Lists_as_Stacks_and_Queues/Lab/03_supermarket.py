from collections import deque

COMMAND_ONE = "End"
COMMAND_TWO = "Paid"
queue = deque()

while True:
    name = input()
    if name == COMMAND_ONE:
        print(f"{len(queue)} people remaining.")
        break
    elif name == COMMAND_TWO:
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)