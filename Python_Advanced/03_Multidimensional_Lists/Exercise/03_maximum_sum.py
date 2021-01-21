def matrix_creator(rows_fun):
    matrix_fun = []
    for row in range(rows_fun):
        lines = [int(x) for x in input().split()]
        matrix_fun.append(lines)
    return matrix_fun


def max_finder(matrix_fun, rows_fun, columns_fun):
    max_sum = -999999999999999999999999999
    for row in range(rows_fun - 2):
        for column in range(columns_fun - 2):
            first = matrix_fun[row][column]
            second = matrix_fun[row][column + 1]
            third = matrix_fun[row][column + 2]
            fourth = matrix_fun[row + 1][column]
            fifth = matrix_fun[row + 1][column + 1]
            sixth = matrix_fun[row + 1][column + 2]
            seventh = matrix_fun[row + 2][column]
            eight = matrix_fun[row + 2][column + 1]
            ninth = matrix_fun[row + 2][column + 2]
            current_sum = first + second + third + fourth + fifth + sixth + seventh + eight + ninth
            if max_sum < current_sum:
                max_sum = current_sum
                square_fun = first, second, third, fourth, fifth, sixth, seventh, eight, ninth
    return square_fun


def printer(square):
    print(f"Sum = {sum(square)}")
    for el in range(0, 7, 3):
        print(f"{square[el]} {square[el + 1]} {square[el + 2]}")


rows, columns = [int(x) for x in input().split()]
matrix = matrix_creator(rows)
square = max_finder(matrix, rows, columns)
printer(square)
