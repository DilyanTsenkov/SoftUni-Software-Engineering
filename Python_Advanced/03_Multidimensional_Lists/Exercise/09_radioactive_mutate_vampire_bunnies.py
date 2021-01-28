def bunnies_finder(liar, rows, cols):
    bunnies = [[row, col] for row in range(rows) for col in range(cols) if liar[row][col] == "B"]
    return bunnies


def bunny_spreader(lair, lair_columns, lair_rows, bunnies):
    for bunny in bunnies:
        row = bunny[0]
        col = bunny[1]
        if col - 1 >= 0:
            lair[row][col - 1] = "B"
        if lair_columns > col + 1:
            lair[row][col + 1] = "B"
        if row - 1 >= 0:
            lair[row - 1][col] = "B"
        if lair_rows > row + 1:
            lair[row + 1][col] = "B"
    return lair


def dead(new_position_col, new_position_row, lair):
    if lair[new_position_row][new_position_col] == "B":
        return True
    return False


def lair_creator(rows):
    lair_fun = [[el for el in input()] for _ in range(rows)]
    return lair_fun


def player_move(lair, pos_row, pos_col, move):
    if move == "L":
        new_pos_col = pos_col - 1
        new_pos_row = pos_row
    elif move == "U":
        new_pos_row = pos_row - 1
        new_pos_col = pos_col
    elif move == "R":
        new_pos_col = pos_col + 1
        new_pos_row = pos_row
    elif move == "D":
        new_pos_row = pos_row + 1
        new_pos_col = pos_col
    lair[pos_row][pos_col] = "."
    return lair, pos_col, pos_row, new_pos_row, new_pos_col


def player_start_position(liar, rows, cols):
    starting = [[row, col] for row in range(rows) for col in range(cols) if liar[row][col] == "P"]
    return starting[0]


def won(new_position_col, new_position_row, lair_columns, lair_rows):
    if lair_columns > new_position_col > -1 and lair_rows > new_position_row > -1:
        return False
    return True


def printer(lair, pos_row, pos_col):
    for row in lair:
        print("".join(row))
    if won(new_pos_col, new_pos_row, lair_columns, lair_rows):
        print(f"won: {pos_row} {pos_col}")
    elif dead(pos_col, pos_row, lair):
        print(f"dead: {pos_row} {pos_col}")


lair_rows, lair_columns = [int(x) for x in input().split()]
lair = lair_creator(lair_rows)
moves = list(input())
pos_row, pos_col = player_start_position(lair, lair_rows, lair_columns)
for move in moves:
    bunnies = bunnies_finder(lair, lair_rows, lair_columns)
    lair, pos_col, pos_row, new_pos_row, new_pos_col = player_move(lair, pos_row, pos_col, move)
    if not won(new_pos_col, new_pos_row, lair_columns, lair_rows):
        if not dead(new_pos_col, new_pos_row, lair):
            lair[new_pos_row][new_pos_col] = "P"
        pos_col = new_pos_col
        pos_row = new_pos_row
    lair = bunny_spreader(lair, lair_columns, lair_rows, bunnies)
    if won(new_pos_col, new_pos_row, lair_columns, lair_rows) or dead(pos_col, pos_row, lair):
        printer(lair, pos_row, pos_col)
        break
