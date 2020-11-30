single_string = input()

single_string_list = single_string.split(", ")
single_string_list.append(single_string_list.pop(single_string_list.index("0")))

for i in range(len(single_string_list)):
    single_string_list[i] = int(single_string_list[i])
for i in range(len(single_string_list)):
    if single_string_list[i] == 0:
        single_string_list.append(single_string_list.pop(single_string_list.index(0)))

print(single_string_list)
