from collections import deque


def coal_on_field(field_fun, side_fun):
    result = 0
    for r in range(side_fun):
        for c in range(side_fun):
            if field_fun[r][c] == "c":
                result += 1
    return result


def c_finder(field_fun, coal_fun, position_row_fun, position_col_fun):
    if field_fun[position_row_fun][position_col_fun] == "c":
        field_fun[position_row_fun][position_col_fun] = "*"
        coal_fun -= 1
    return coal_fun


def e_finder(field_fun, position_row_fun, position_col_fun):
    if field_fun[position_row_fun][position_col_fun] == "e":
        return True


def field_creator(side_fun):
    field_fun = []
    for row in range(side_fun):
        lines = input().split()
        field_fun.append(lines)
    return field_fun


def position(field_fun, side_fun):
    starting = []
    for i in range(side_fun):
        for n in range(side_fun):
            if field_fun[i][n] == "s":
                starting.append(i)
                starting.append(n)
    return starting


def miner_move(position_row_fun, position_col_fun, move_fun, side_fun):
    if move_fun == "left" and position_col_fun > 0:
        position_col_fun -= 1
    elif move_fun == "right" and position_col_fun < side_fun - 1:
        position_col_fun += 1
    elif move_fun == "up" and position_row_fun > 0:
        position_row_fun -= 1
    elif move_fun == "down" and position_row_fun < side_fun - 1:
        position_row_fun += 1
    return position_row_fun, position_col_fun


def the_end(game_over, coal, moves):
    result = True
    if game_over:
        print(f"Game over! ({position_row}, {position_col})")
    elif coal == 0:
        print(f"You collected all coals! ({position_row}, {position_col})")
    elif not moves:
        print(f"{coal} coals left. ({position_row}, {position_col})")
    else:
        result = False
    return result


side = int(input())
moves = deque(input().split())
field = field_creator(side)
coal = coal_on_field(field, side)
position_row, position_col = position(field, side)
for m in range(len(moves)):
    move = moves.popleft()
    position_row, position_col = miner_move(position_row, position_col, move, side)
    coal = c_finder(field, coal, position_row, position_col)
    game_over = e_finder(field, position_row, position_col)
    if the_end(game_over, coal, moves):
        break
