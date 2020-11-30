operator = input()
first_number = int(input())
second_number = int(input())


def calculation(first_num, second_num, opr):
    result = None
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = int(first_number / second_number)
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    return result


print(calculation(first_number, second_number, operator))
