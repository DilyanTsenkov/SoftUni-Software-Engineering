def organizer(numbers):
    return sorted(numbers)


numbers = [int(el) for el in input().split()]
print(organizer(numbers))
