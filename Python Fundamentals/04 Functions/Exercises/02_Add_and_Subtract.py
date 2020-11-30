def add_and_subtract(first_num, second_num, third_num):
    def sum_numbers(first, second):
        return first + second

    def subtract(sum_number, third):
        return (sum_numbers(first_num, second_num)) - third

    return subtract(sum_numbers, third_num)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
