import math


def field_creator(side):
    field = [[el for el in input().split()] for _ in range(side)]
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
    if validator(field, possible_player_row, possible_player_col, side):
        return possible_player_row, possible_player_col, True
    else:
        return player_row, player_col, False


def validator(field, player_row, player_col, side):
    if 0 <= player_row < side and 0 <= player_col < side and field[player_row][player_col] != "X":
        return True
    return False


def printer(coins, path):
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
    else:
        print(f"Game over! You've collected {coins} coins.")
    print("Your path:")
    for step in path:
        print(step)


side = int(input())
field = field_creator(side)
player_row, player_col = player_position(field, side)
coins = 0
path = []
while coins < 100:
    command = input()
    player_row, player_col, is_valid = movement(field, side, player_row, player_col, command)
    if is_valid:
        step = [player_row, player_col]
        path.append(step)
        coins += int(field[player_row][player_col])
    else:
        coins = math.floor(coins / 2)
        break
printer(coins, path)
