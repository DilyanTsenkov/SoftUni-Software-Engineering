from collections import deque

quantity = int(input())
orders = input().split()
orders = [int(el) for el in orders]

queue = deque(orders)

print(max(queue))

while queue:
    order = queue.popleft()
    if quantity >= order:
        quantity -= order
    else:
        queue.reverse()
        queue.append(order)
        break

if queue:
    queue.reverse()
    to_print = ""
    while queue:
        to_print += str(queue.popleft()) + " "
    print(f"Orders left: {to_print.strip()}")
else:
    print("Orders complete")
