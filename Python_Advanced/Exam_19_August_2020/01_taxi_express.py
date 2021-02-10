from collections import deque

customers = deque(input().split(", "))
taxis = input().split(", ")

drive_time = 0

while True:
    customer = customers.popleft()
    taxi = taxis.pop()
    if int(customer) > int(taxi):
        customers.appendleft(customer)
    else:
        drive_time += int(customer)
    if not customers or not taxis:
        break

if customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(customers)}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {drive_time} minutes")
