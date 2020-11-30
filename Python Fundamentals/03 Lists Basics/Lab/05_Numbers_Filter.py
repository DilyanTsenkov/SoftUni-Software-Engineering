number = int(input())

my_list = []
print_list = []

for num in range(number):
    integer = int(input())
    my_list.append(integer)

command = input()

for i in range(len(my_list)):
    if command == "even":
        if my_list[i] % 2 == 0:
            print_list.append(my_list[i])
    elif command == "odd":
        if my_list[i] % 2 != 0:
            print_list.append(my_list[i])
    elif command == "negative":
        if my_list[i] < 0:
            print_list.append(my_list[i])
    elif command == "positive":
        if my_list[i] >= 0:
            print_list.append(my_list[i])

print(print_list)