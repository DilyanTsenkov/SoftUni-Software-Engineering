def even(numbers):
    if numbers % 2 == 0:
        return True


def odd(numbers):
    if numbers % 2 != 0:
        return True


def printer(nums, numbers):
    print(sum(nums) * len(numbers))


command = input()
numbers = [int(el) for el in input().split()]
if command == "Odd":
    odd_numbers = list(filter(odd, numbers))
    printer(odd_numbers, numbers)

elif command == "Even":
    even_numbers = list(filter(even, numbers))
    printer(even_numbers, numbers)
