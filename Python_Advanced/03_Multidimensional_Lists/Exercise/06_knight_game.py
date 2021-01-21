def matrix_creator(board_side_fun):
    matrix_fun = []
    for row in range(board_side_fun):
        lines = list(input())
        matrix_fun.append(lines)
    return matrix_fun


def index_validator(move_r_fun, move_c_fun, board_side):
    if 0 <= move_r_fun < board_side and 0 <= move_c_fun < board_side:
        return True
    return False


def movement(matrix_fun, r_fun, c_fun, board_side_fun):
    hits_fun = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    columns = [-1, 1, -1, 1, -2, 2, -2, 2]
    for i in range(len(rows)):
        move_r = r_fun + rows[i]
        move_c = c_fun + columns[i]
        if index_validator(move_r, move_c, board_side_fun):
            if matrix_fun[move_r][move_c] == "K":
                hits_fun += 1
    return hits_fun


counter = 0
board_side = int(input())
matrix = matrix_creator(board_side)
while True:
    max_hits = 0
    position_max_hits = []
    for r in range(board_side):
        for c in range(board_side):
            if matrix[r][c] == "K":
                hits = movement(matrix, r, c, board_side)
                if max_hits < hits:
                    max_hits = hits
                    position_max_hits = [r, c]
    if max_hits > 0:
        matrix[position_max_hits[0]][position_max_hits[1]] = "0"
        counter += 1
    else:
        break
print(counter)
