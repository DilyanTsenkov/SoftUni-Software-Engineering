first_pair = int(input())
second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())
for first in range(first_pair, first_pair + diff_first_pair + 1):
    first_prime = 0
    for i in range(2, first):
        if (first % i) == 0:
            break
    else:
        first_prime = first
    for second in range(second_pair, second_pair + diff_second_pair + 1):
        if first_prime == 0:
            break
        for i in range(2, second):
            if (second % i) == 0:
                break
        else:
            second_prime = second
            print(f"{first_prime}{second_prime}")

