def add(matrix, row, col, value):
    matrix[row][col] += value
    return matrix


def coord_validator(rows, row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


def matrix_creator(rows):
    matrix = [[int(el) for el in input().split()] for _ in range(rows)]
    return matrix


def printer(matrix):
    [print(*row) for row in matrix]


def subtract(matrix, row, col, value):
    matrix[row][col] -= value
    return matrix


def the_end(command):
    if command == "END":
        return True


rows = int(input())
matrix = matrix_creator(rows)

while True:
    command = input()
    if the_end(command):
        break
    command = command.split()
    action = command.pop(0)
    row, col, value = [int(el) for el in command]
    if not coord_validator(rows, row, col):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix = add(matrix, row, col, value)
        else:
            matrix = subtract(matrix, row, col, value)
printer(matrix)
