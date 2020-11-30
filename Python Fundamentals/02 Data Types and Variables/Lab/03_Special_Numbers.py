number = int(input())

for num in range(1, number + 1):
    sum = 0
    for symbol in str(num):
        sum += int(symbol)
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
