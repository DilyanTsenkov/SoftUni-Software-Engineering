def func_executor(*args):
    result = []
    for arg in args:
        function = arg[0]
        result.append(function(*arg[1]))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)),(sum_numbers, (1, 2))))
