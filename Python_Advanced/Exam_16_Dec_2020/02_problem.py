def field_creator(side):
    field = [[el for el in input()] for _ in range(side)]
    return field


def player_position(field, side):
    for row in range(side):
        if "P" in field[row]:
            col = field[row].index("P")
            break
    return row, col


def movement(field, side, player_row, player_col, command):
    if command == "right":
        possible_player_col = player_col + 1
        possible_player_row = player_row
    elif command == "left":
        possible_player_col = player_col - 1
        possible_player_row = player_row
    elif command == "down":
        possible_player_row = player_row + 1
        possible_player_col = player_col
    elif command == "up":
        possible_player_row = player_row - 1
        possible_player_col = player_col
    if validator(possible_player_row, possible_player_col, side):
        field[player_row][player_col] = "-"
        return possible_player_row, possible_player_col, True
    else:
        return player_row, player_col, False


def validator(player_row, player_col, side):
    if 0 <= player_row < side and 0 <= player_col < side:
        return True
    return False


def printer(field, string):
    print(string)
    for row in field:
        print("".join(row))


string = input()
side = int(input())

field = field_creator(side)
player_row, player_col = player_position(field, side)

commands = int(input())
for _ in range(commands):
    command = input()
    player_row, player_col, is_valid = movement(field, side, player_row, player_col, command)
    if is_valid:
        if field[player_row][player_col] != "-":
            string += field[player_row][player_col]
            field[player_row][player_col] = "P"
    else:
        string = string[:-1]
printer(field, string)