def matrix_creator(side_fun):
    matrix_fun = []
    for row in range(side_fun):
        lines = [int(x) for x in input().split()]
        matrix_fun.append(lines)
    return matrix_fun


def bombs_organizer(bombs_fun):
    bombs_fun = bombs_fun.split()
    for i in range(len(bombs_fun)):
        bombs_fun[i] = [int(x) for x in bombs_fun[i].split(",")]
    return bombs_fun


def current_bomb(matrix_fun, bomb_fun):
    row_fun = bomb_fun[0]
    col_fun = bomb_fun[1]
    bomb_damage_fun = matrix_fun[row_fun][col_fun]
    return row_fun, col_fun, bomb_damage_fun


def demolisher(matrix_fun, side_fun, bomb_damage_fun, row_fun, col_fun):
    for r in range(side_fun):
        for c in range(side_fun):
            if row == r or r == row_fun - 1 or r == row_fun + 1:
                if c == col or c == col_fun - 1 or c == col_fun + 1:
                    if matrix_fun[r][c] > 0:
                        matrix_fun[r][c] -= bomb_damage_fun
    return matrix_fun


def alive_finder(matrix_fun):
    finder = 0
    amount = 0
    for row_fun in matrix_fun:
        for el in row_fun:
            if el > 0:
                finder += 1
                amount += el
    return finder, amount


def printer(matrix, alive_count, alive_amount):
    print(f"Alive cells: {alive_count}")
    print(f"Sum: {alive_amount}")
    for row_fun in matrix:
        row_fun = [str(x) for x in row_fun]
        print(" ".join(row_fun))


side = int(input())
matrix = matrix_creator(side)
bombs = input()
bombs = bombs_organizer(bombs)
for bomb in bombs:
    row, col, bomb_damage = current_bomb(matrix, bomb)
    if bomb_damage <= 0:
        continue
    matrix = demolisher(matrix, side, bomb_damage, row, col)
alive_count, alive_amount = alive_finder(matrix)
printer(matrix, alive_count, alive_amount)
