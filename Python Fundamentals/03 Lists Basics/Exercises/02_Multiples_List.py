first_number = int(input())
second_number = int(input())

numbers_list = []

for num in range(1, (first_number * second_number) + 1):
    if num % first_number == 0:
        numbers_list.append(num)

print(numbers_list)
