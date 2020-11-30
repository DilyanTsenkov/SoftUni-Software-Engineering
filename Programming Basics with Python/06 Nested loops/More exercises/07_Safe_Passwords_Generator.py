a = int(input())
b = int(input())
max_pass = int(input())
passwords = 0
counter_first_last_symbol = 0
counter_second_last_symbol = 0
breaker = False
for third_symbol in range(1, a + 1):
    for fourth_symbol in range(1, b + 1):
        first_last_symbol = 35 + counter_first_last_symbol
        second_last_symbol = 64 + counter_second_last_symbol
        if first_last_symbol > 55:
            first_last_symbol = 35
            counter_first_last_symbol = 0
        if second_last_symbol > 96:
            second_last_symbol = 64
            counter_second_last_symbol = 0
        print(
            f"{chr(first_last_symbol)}{chr(second_last_symbol)}{third_symbol}{fourth_symbol}\
{chr(second_last_symbol)}{chr(first_last_symbol)}", end="|")
        passwords += 1
        counter_first_last_symbol += 1
        counter_second_last_symbol += 1
        if passwords == max_pass:
            breaker = True
            break
    if breaker:
        break
