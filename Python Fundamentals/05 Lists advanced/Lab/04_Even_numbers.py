string = input().split(", ")

even = [index for index in range(len(string)) if int(string[index]) % 2 == 0]

print(even)
