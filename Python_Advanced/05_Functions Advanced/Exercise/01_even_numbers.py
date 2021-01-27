def even(numbers):
    if numbers % 2 == 0:
        return True


numbers = [int(el) for el in input().split()]
filtered_numbers = filter(even, numbers)

print(list(filtered_numbers))
