string_of_numbers = input()
number = int(input())

list_of_numbers = string_of_numbers.split(" ")

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])

for n in range(number):
    min_number = min(list_of_numbers)
    list_of_numbers.remove(min_number)

print(list_of_numbers)
