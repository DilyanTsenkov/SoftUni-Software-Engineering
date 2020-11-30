string = input()

string_list = string.split()
string_list_print = []

for index in range(len(string_list)):
    number = int(string_list[index]) * -1
    string_list_print.append(number)
    
print(string_list_print)
