def matrix_creator(rows_fun):
    matrix_fun = []
    for _ in range(rows_fun):
        line = [int(x) for x in input().split()]
        matrix_fun.append(line)
    return matrix_fun


def diagonal_sum(matrix_fun, rows_fun):
    result = 0
    for row in range(rows_fun):
        result += matrix_fun[row][row]
    print(result)


rows = int(input())
matrix = matrix_creator(rows)
diagonal_sum(matrix, rows)
