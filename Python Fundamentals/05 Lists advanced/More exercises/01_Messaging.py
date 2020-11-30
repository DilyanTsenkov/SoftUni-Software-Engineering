numbers = input().split()
string = list(input())

print_string = ""

for el in numbers:
    sum_of_numbers = 0
    for i in el:
        sum_of_numbers += int(i)

    if sum_of_numbers < len(string):
        print_string += string.pop(sum_of_numbers)
    else:
        n = sum_of_numbers % (len(string))
        print_string += string.pop(n)

print(print_string)
