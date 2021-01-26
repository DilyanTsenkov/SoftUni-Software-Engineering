from functools import reduce


def operate(opr, *args):
    operators = {
        "+": reduce(lambda x, y: x + y, args),
        "-": reduce(lambda x, y: x - y, args),
        "*": reduce(lambda x, y: x * y, args),
        "/": reduce(lambda x, y: x / y, args)
    }
    return operators[opr]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

