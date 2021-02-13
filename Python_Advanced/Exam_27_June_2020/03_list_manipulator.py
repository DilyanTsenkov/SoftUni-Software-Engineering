from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    add_remove = args[0]
    beginning_end = args[1]
    others = args[2::]

    if add_remove == "add" and beginning_end == "beginning":
        others = list(others[::-1])
        for el in others:
            numbers.appendleft(el)
    elif add_remove == "add" and beginning_end == "end":
        for el in others:
            numbers.append(el)
    elif add_remove == "remove" and beginning_end == "beginning":
        if others:
            for _ in range(others[0]):
                numbers.popleft()
        else:
            numbers.popleft()
    elif add_remove == "remove" and beginning_end == "end":
        if others:
            for _ in range(others[0]):
                numbers.pop()
        else:
            numbers.pop()
    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
