first_number_max = int(input())
second_number_max = int(input())
third_number_max = int(input())
for first_number in range(1, first_number_max + 1):
    if first_number % 2 == 1:
        continue
    for second_number in range(2, second_number_max + 1):
        if second_number == 4 or second_number == 6 or second_number > 7:
            continue
        for third_number in range(1, third_number_max + 1):
            if third_number % 2 == 1:
                continue
            print(first_number, second_number, third_number)
