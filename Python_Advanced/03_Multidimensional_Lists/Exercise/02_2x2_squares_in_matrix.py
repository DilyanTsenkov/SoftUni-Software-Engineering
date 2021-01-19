def matrix_creator(rows_fun):
    matrix_fun = []
    for _ in range(rows_fun):
        line = input().split()
        matrix_fun.append(line)
    return matrix_fun


def finder(matrix_fun, rows_fun, columns_fun):
    counter_fun = 0
    for row in range(rows_fun - 1):
        for column in range(columns_fun - 1):
            first = matrix_fun[row][column]
            second = matrix_fun[row + 1][column]
            third = matrix_fun[row][column + 1]
            fourth = matrix_fun[row + 1][column + 1]
            if first == second == third == fourth:
                counter_fun += 1
    return counter_fun


rows, columns = [int(x) for x in input().split()]
matrix = matrix_creator(rows)
counter = finder(matrix, rows, columns)
print(counter)
