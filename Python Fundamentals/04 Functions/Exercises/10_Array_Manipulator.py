import sys

list_input = input().split()
command = input()
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
while command != "end":
    command_list = command.split()
    result = []


    def exchange(list_input, index):
        if index >= len(list_input):
            print("Invalid index")
            return list_input
        elif index < 0:
            print("Invalid index")
            return list_input
        else:
            a_list = list_input[0:index + 1]
            b_list = list_input[index + 1:]
            list_input = b_list + a_list
            return list_input


    if command_list[0] == "exchange":
        list_input = exchange(list_input, int(command_list[-1]))


    def maximum_even_odd(list_input):
        max_num_even = -1
        max_num_odd = -1
        for i in range(len(list_input)):
            if list_input[i] % 2 == 0:
                if list_input[i] >= max_num_even:
                    max_num_even = list_input[i]
                    max_num_even_index = i
            elif list_input[i] % 2 != 0:
                if list_input[i] >= max_num_odd:
                    max_num_odd = list_input[i]
                    max_num_odd_index = i
        if command_list[-1] == "even":
            if max_num_even == -1:
                result = "No matches"
            else:
                result = max_num_even_index
            return result
        else:
            if max_num_odd == -1:
                result = "No matches"
            else:
                result = max_num_odd_index
            return result


    if command_list[0] == "max":
        print(maximum_even_odd(list_input))


    def minimum_even_odd(list_input):
        min_num_even = sys.maxsize
        min_num_odd = sys.maxsize
        for i in range(len(list_input)):
            if list_input[i] % 2 == 0:
                if list_input[i] <= min_num_even:
                    min_num_even = list_input[i]
                    min_num_even_index = i
            elif list_input[i] % 2 != 0:
                if list_input[i] <= min_num_odd:
                    min_num_odd = list_input[i]
                    min_num_odd_index = i
        if command_list[-1] == "even":
            if min_num_even == sys.maxsize:
                result = "No matches"
            else:
                result = min_num_even_index
            return result
        if command_list[-1] == "odd":
            if min_num_odd == sys.maxsize:
                result = "No matches"
            else:
                result = min_num_odd_index
            return result


    if command_list[0] == "min":
        print(minimum_even_odd(list_input))


    def first_even_odd(list_input, index):
        if int(index) > len(list_input):
            return "Invalid count"
        even_list = []
        odd_list = []
        for i in range(len(list_input)):
            if list_input[i] % 2 == 0:
                even_list.append(list_input[i])
            if list_input[i] % 2 != 0:
                odd_list.append(list_input[i])
        if command_list[0] == "first":
            if command_list[2] == "even":
                return even_list[:index]
            else:
                return odd_list[:index]
        if command_list[0] == "last":
            if command_list[2] == "even":
                return even_list[-index:]
            else:
                return odd_list[-index:]


    if command_list[0] == "first" or command_list[0] == "last":
        print(first_even_odd(list_input, int(command_list[1])))

    command = input()
print(list_input)
