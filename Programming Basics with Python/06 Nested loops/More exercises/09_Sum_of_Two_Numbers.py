interval_start = int(input())
interval_end = int(input())
magick_number = int(input())
counter = 0
breaker = False
for number_one in range(interval_start, interval_end + 1):
    for number_two in range(interval_start, interval_end + 1):
        counter += 1
        if number_one + number_two == magick_number:
            sum = number_one + number_two
            print(f"Combination N:{counter} ({number_one} + {number_two} = {sum})")
            breaker = True
            break
    if breaker:
        break
if not breaker:
    print(f"{counter} combinations - neither equals {magick_number}")