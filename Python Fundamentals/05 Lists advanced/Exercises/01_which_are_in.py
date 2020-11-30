first_list = input().split(", ")
second_list = input().split(", ")

unique_values_list = []

for el in first_list:
    for k in second_list:
        if k.find(el) >= 0 and el not in unique_values_list:
            unique_values_list.append(el)

print(unique_values_list)
