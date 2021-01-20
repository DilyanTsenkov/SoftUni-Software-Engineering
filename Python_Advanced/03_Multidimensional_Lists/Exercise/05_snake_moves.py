from collections import deque


def snake_walk(rows_fun, columns_fun, snake_fun):
    matrix_fun = []
    for row in range(rows_fun):
        matrix_row = []
        for column in range(columns_fun):
            char = snake_fun.popleft()
            matrix_row.append(char)
            snake_fun.append(char)
        if row % 2 != 0:
            matrix_fun.append(matrix_row[::-1])
        else:
            matrix_fun.append(matrix_row)
    return matrix_fun


def printer(snake_matrix):
    for el in snake_matrix:
        print("".join(el))


rows, columns = [int(x) for x in input().split()]
snake = deque(input())
snake_matrix = snake_walk(rows, columns, snake)
printer(snake_matrix)
