def matrix_creator(rows_fun):
    matrix_fun = []
    for row in range(rows_fun):
        lines = input().split()
        matrix_fun.append(lines)
    return matrix_fun


rows, columns = [int(x) for x in input().split()]
matrix = matrix_creator(rows)

while True:
    command = input()
    if command == "END":
        break
    command_line = command.split()
    if command_line[0] == "swap" and len(command_line) == 5:
        command_line.pop(0)
        r1, c1, r2, c2 = [int(x) for x in command_line]
        if -1 < r1 < rows and -1 < r2 < rows and -1 < c1 < columns and -1 < c2 < columns:
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in range(rows):
                print(f"{' '.join(matrix[row])}")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
