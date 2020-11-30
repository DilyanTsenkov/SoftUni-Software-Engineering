n = int(input())
sum_of_numbers = 0
for number in range(n):
    input_number = int(input())
    sum_of_numbers += input_number
average = sum_of_numbers / n
print(f"{average:.2f}")
