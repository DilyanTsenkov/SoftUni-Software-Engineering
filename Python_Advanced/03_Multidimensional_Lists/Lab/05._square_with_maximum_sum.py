def matrix_creator(rows_fun):
    matrix_fun = []
    for row in range(rows_fun):
        lines = [int(x) for x in input().split(", ")]
        matrix_fun.append(lines)
    return matrix_fun


def max_finder(matrix_fun, rows_fun, columns_fun):
    max_one = 0
    for row in range(rows_fun - 1):
        for column in range(columns_fun - 1):
            first = matrix_fun[row][column]
            second = matrix_fun[row][column + 1]
            third = matrix_fun[row + 1][column]
            fourth = matrix_fun[row + 1][column + 1]
            sums = first + second + third + fourth
            if max_one < sums:
                max_one = sums
                square_fun = first, second, third, fourth
    return square_fun


def printer(square):
    for el in range(0, 3, 2):
        print(f"{square[el]} {square[el + 1]}")
    print(sum(square))


rows, columns = [int(x) for x in input().split(", ")]
matrix = matrix_creator(rows)
square = max_finder(matrix, rows, columns)
printer(square)
