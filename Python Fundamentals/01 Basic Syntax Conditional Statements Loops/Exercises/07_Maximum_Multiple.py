divisor = int(input())
bound = int(input())

max_number = 0

for n in range(1, bound + 1):
    if n % divisor == 0:
        if max_number < n:
            max_number = n

print(max_number)
