def create_matrix(side):
    matrix_fun = []
    for _ in range(side):
        line = [int(x) for x in input().split()]
        matrix_fun.append(line)
    return matrix_fun


def primary_diagonal(matrix_fun, side):
    primary_sum = 0
    for row in range(side):
        primary_sum += matrix_fun[row][row]
    return primary_sum


def secondary_diagonal(matrix_fun, side):
    secondary_sum = 0
    for row in range(0, side):
        secondary_sum += matrix_fun[row][abs(side - 1 - row)]
    return secondary_sum


def printer(primary, secondary):
    print(abs(primary - secondary))


matrix_side = int(input())
matrix = create_matrix(matrix_side)
primary = primary_diagonal(matrix, matrix_side)
secondary = secondary_diagonal(matrix, matrix_side)
printer(primary, secondary)
