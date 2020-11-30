n = int(input())
first_sum = 0
second_sum = 0
difference = 0
max_difference = 0
previous_number = 0
for number in range(1, 2 * n + 1):
    new_number = int(input())
    if number % 2 == 0:
        first_sum = previous_number + new_number
        if number > 2:
            difference = abs(second_sum - first_sum)
            if difference >= max_difference:
                max_difference = difference
    previous_number = new_number
    second_sum = first_sum
if max_difference == 0:
    print(f'Yes, value={first_sum}')
else:
    print(f'No, maxdiff={max_difference}')

#--------------------------------------------------
# n = int(input())
# sum = 0
# old_sum = 0
# new_sum = 0
# difference = 0
# old_difference = 0
# print_difference = 0
# for numbers in range(0, n):
#     number_one = int(input())
#     number_two = int(input())
#     if numbers == 0:
#         old_sum = number_one + number_two
#         sum += old_sum
#     else:
#         new_sum = number_one + number_two
#         if new_sum == old_sum:
#             sum += old_sum
#         difference = abs(new_sum - old_sum)
#         if difference >= old_difference:
#             print_difference = difference
#         old_sum = new_sum
#         old_difference = difference
# if old_sum * n == sum:
#     print(f'Yes, value={old_sum}')
# else:
#     print(f'No, maxdiff={print_difference}')
