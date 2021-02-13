def territory_generator(side):
    territory = []
    for _ in range(side):
        row = [char for char in input()]
        territory.append(row)
    return territory


def snake_position(territory, side):
    for row in range(side):
        for col in range(side):
            if territory[row][col] == "S":
                snake_row_position = row
                snake_col_position = col
    return snake_row_position, snake_col_position


def mover(command, snake_row_position, snake_col_position):
    if command == "left":
        snake_col_position -= 1
    elif command == "right":
        snake_col_position += 1
    elif command == "down":
        snake_row_position += 1
    elif command == "up":
        snake_row_position -= 1
    return snake_row_position, snake_col_position


def not_out_of_territory(snake_row_position, snake_col_position, side):
    if snake_row_position < 0 or snake_col_position < 0 or snake_row_position == side or snake_col_position == side:
        return False
    return True


def b_finder(territory, side):
    for row in range(side):
        for col in range(side):
            if territory[row][col] == "B":
                b_row_position = row
                b_col_position = col
    return b_row_position, b_col_position


def printer(food_eaten, territory):
    if food_eaten == 10:
        print("You won! You fed the snake.")
    else:
        print("Game over!")
    print(f"Food eaten: {food_eaten}")
    for row in territory:
        print("".join(row))


side = int(input())
territory = territory_generator(side)
snake_row_position, snake_col_position = snake_position(territory, side)
food_eaten = 0
while food_eaten != 10:
    command = input()
    territory[snake_row_position][snake_col_position] = "."
    snake_row_position, snake_col_position = mover(command, snake_row_position, snake_col_position)
    if not_out_of_territory(snake_row_position, snake_col_position, side):
        if territory[snake_row_position][snake_col_position] == "*":
            food_eaten += 1
            territory[snake_row_position][snake_col_position] = "S"
        if territory[snake_row_position][snake_col_position] == "B":
            territory[snake_row_position][snake_col_position] = "."
            snake_row_position, snake_col_position = b_finder(territory, side)
        territory[snake_row_position][snake_col_position] = "S"
    else:
        break
printer(food_eaten, territory)
