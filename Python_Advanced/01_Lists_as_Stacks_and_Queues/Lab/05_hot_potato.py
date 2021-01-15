from collections import deque

kids = input().split()
passing = int(input())

queue = deque(kids)

while len(queue) > 1:
    for _ in range(passing - 1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.popleft()}")
