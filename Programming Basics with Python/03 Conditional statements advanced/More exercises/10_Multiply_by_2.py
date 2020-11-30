count = 0
while (count >= 0):
    count = float(input())
    if count >= 0:
        print(f"Result: {(count * 2):.2f}")
    else:
        print(f"Negative number!")
