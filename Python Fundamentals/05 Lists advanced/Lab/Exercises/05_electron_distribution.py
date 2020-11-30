electrons = int(input())

index = 0
shell_list = []

while electrons > 0:
    index += 1
    max_num_electrons = 2 * index ** 2
    if electrons >= max_num_electrons:
        shell_list.append(max_num_electrons)
        electrons -= max_num_electrons
    else:
        shell_list.append(electrons)
        electrons -= max_num_electrons

print(shell_list)