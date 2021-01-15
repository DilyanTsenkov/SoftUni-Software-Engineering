stack = input().split()
stack = [int(el) for el in stack]

capacity = int(input())
value = 0
counter = 0

while stack:
    cloth = stack.pop()
    value += cloth
    if capacity == value:
        if len(stack) > 0:
            counter += 1
            value = 0
    elif capacity < value:
        value = cloth
        counter += 1

if value > 0:
    counter += 1
print(counter)
