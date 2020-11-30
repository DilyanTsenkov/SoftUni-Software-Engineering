maze_rows = int(input())

maze = [list(input()) for row in range(maze_rows)]

for row_k in range(maze_rows):
    if "k" in maze[row_k]:
        place_of_k = [row_k, maze[row_k].index("k")]

no_way_out = False
break_flag = False

moves = 0

while True:
    if break_flag:
        moves += 1
        break
    no_more_col = True
    no_more_row = True
    while True:
        for column in range(place_of_k[1] - 1, place_of_k[1] + 2):
            no_more_col = True
            if " " not in maze[place_of_k[0]]:
                break
            if maze[place_of_k[0]][column] == " ":
                maze[place_of_k[0]][place_of_k[1]] = "*"
                maze[place_of_k[0]][column] = "k"
                place_of_k = [place_of_k[0], column]
                no_more_col = False
                moves += 1
                break
        for el in range(len(maze)):
            if ((maze[el][0] == "k" and maze[el][1] != " ") and (
                    maze[el][0] == "k" and maze[el + 1][0] != " ") and (
                        maze[el][0] == "k" and maze[el - 1][0] != " ")) or (
                    (maze[el][-1] == "k" and maze[el][-2] != " ") and (
                    maze[el][-1] == "k" and maze[el + 1][-2] != " ") and (
                            maze[el][-1] == "k" and maze[el - 1][-2] != " ")):
                break_flag = True
                no_more_col = False
                break
        break

    while True:
        for row in range(place_of_k[0] - 1, place_of_k[0] + 2):
            no_more_row =True
            if row < 0:
                continue
            if "k" in maze[maze_rows - 1] and " " not in maze[maze_rows - 2]:
                break
            if maze[row][place_of_k[1]] == " ":
                maze[place_of_k[0]][place_of_k[1]] = "*"
                maze[row][place_of_k[1]] = "k"
                place_of_k = [row, place_of_k[1]]
                no_more_row = False
                moves += 1
                break
        if ("k" in maze[0] and " " not in maze[0]) or ("k" in maze[maze_rows - 1] and " " not in maze[maze_rows - 1]):
            break_flag = True
            break
        break
    if no_more_col and no_more_row:
        no_way_out = True
        break
if no_way_out:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {moves} moves")