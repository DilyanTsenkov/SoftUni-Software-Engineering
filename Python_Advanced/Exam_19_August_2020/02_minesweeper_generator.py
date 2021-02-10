def mine_field_creator(square_side):
    mine_field = [[" " for _ in range(square_side)] for _ in range(square_side)]
    return mine_field


def put_mines_on_field(mine_field):
    bombs_count = int(input())
    for _ in range(bombs_count):
        bomb = input()[1:-1]
        bomb_row, bomb_col = [int(current_bomb) for current_bomb in bomb.split(", ")]
        mine_field[bomb_row][bomb_col] = "*"
    return mine_field


def validator(r, c, length):
    if 0 <= r < length and 0 <= c < length:
        return True
    return False


def cell_calculator(mine_field, row, col):
    value = 0
    for possible_row in range(-1, 2):
        for possible_col in range(-1, 2):
            if validator(row + possible_row, col + possible_col, square_side):
                if mine_field[row + possible_row][col + possible_col] == "*":
                    value += 1
    mine_field[row][col] = str(value)
    return mine_field


def printer(mine_field):
    for row in mine_field:
        print(' '.join(row))


square_side = int(input())
mine_field = mine_field_creator(square_side)
put_mines_on_field(mine_field)
for row in range(square_side):
    for col in range(square_side):
        if mine_field[row][col] != "*":
            mine_field = cell_calculator(mine_field, row, col)
printer(mine_field)
