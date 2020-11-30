interval_start = int(input())
interval_end = int(input())
for first_digit in range(interval_start, interval_end + 1):
    for second_digit in range(interval_start, interval_end + 1):
        for third_digit in range(interval_start, interval_end + 1):
            if (second_digit + third_digit) % 2 != 0:
                continue
            for fourth_digit in range(interval_start, interval_end + 1):
                if first_digit > fourth_digit:
                    if first_digit % 2 == 0:
                        if fourth_digit % 2 == 0:
                            continue
                    if first_digit % 2 == 1:
                        if fourth_digit % 2 == 1:
                            continue
                    print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")
