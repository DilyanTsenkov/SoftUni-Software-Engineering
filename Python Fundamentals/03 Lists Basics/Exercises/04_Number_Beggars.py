numbers_list = input().split(", ")
beggars = int(input())

numbers_list_print = []
begin_from = 0
sum_numbers = 0

for beggar in range(beggars):

    for i in range(begin_from, len(numbers_list), beggars):
        sum_numbers += int(numbers_list[i])

    numbers_list_print.append(sum_numbers)
    sum_numbers = 0
    begin_from += 1

print(numbers_list_print)
