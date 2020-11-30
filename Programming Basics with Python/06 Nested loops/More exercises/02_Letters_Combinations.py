interval_start = input()
interval_end = input()
skip_letter = input()
counter = 0
for first_char in range(ord(interval_start), ord(interval_end) + 1):
    if first_char == ord(skip_letter):
        continue
    for second_char in range(ord(interval_start), ord(interval_end) + 1):
        if second_char == ord(skip_letter):
            continue
        for third_char in range(ord(interval_start), ord(interval_end) + 1):
            if third_char == ord(skip_letter):
                continue
            counter += 1
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}", end=" ")
print(counter)
