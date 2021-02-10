def numbers_searching(*args):
    numbers = [int(arg) for arg in args]

    max_number = max(numbers)
    min_number = min(numbers)
    range_to_check = max_number - min_number

    counter = 1
    current_number = min_number + counter
    missing_numbers = []
    for _ in range(range_to_check - 1):
        if current_number not in numbers:
            missing_numbers.append(current_number)
        current_number += 1

    duplicate_numbers = []
    for number in numbers:
        counter = numbers.count(number)
        if counter > 1:
            duplicate_numbers.append(number)
    duplicate_numbers = set(duplicate_numbers)
    duplicate_numbers = sorted(list(duplicate_numbers))

    result = missing_numbers
    result.append(duplicate_numbers)
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
