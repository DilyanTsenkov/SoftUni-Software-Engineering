def matrix_creator(n_fun):
    matrix_fun = []
    for row_fun in range(n_fun):
        characters_fun = [x for x in input()]
        matrix_fun.append(characters_fun)
    return matrix_fun


def finder(matrix_fun, symbol_fun):
    find = False
    for row in range(n):
        if find:
            break
        for col in range(n):
            if matrix_fun[row][col] == symbol_fun:
                find = True
                print(f"({row}, {col})")
                break
    return find


n = int(input())
matrix = matrix_creator(n)
symbol = input()
find = finder(matrix, symbol)
if not find:
    print(f"{symbol} does not occur in the matrix")
