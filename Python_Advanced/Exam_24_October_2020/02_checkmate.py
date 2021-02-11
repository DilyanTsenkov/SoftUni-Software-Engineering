def board_creator():
    chess_board = [input().split() for _ in range(8)]
    return chess_board


def king_place(chess_board):
    for row in range(8):
        for col in range(8):
            if chess_board[row][col] == "K":
                return row, col


def row_checker(chess_board, k_row, k_col, queens_can_capture):
    for i in range(-1, 2, 2):
        temp_c = k_col + i
        while 0 <= temp_c < 8:
            if chess_board[k_row][temp_c] == "Q":
                queen_coord = [k_row, temp_c]
                queens_can_capture.append(queen_coord)
                break
            temp_c += i
    return queens_can_capture


def col_checker(chess_board, k_row, k_col, queens_can_capture):
    for i in range(-1, 2, 2):
        temp_r = k_row + i
        while 0 <= temp_r < 8:
            if chess_board[temp_r][k_col] == "Q":
                queen_coord = [temp_r, k_col]
                queens_can_capture.append(queen_coord)
                break
            temp_r += i
    return queens_can_capture


def diagonals_checker(chess_board, k_row, k_col, signs, queens_can_capture):
    for _ in range(4):
        temp_r = k_row + signs[0]
        temp_c = k_col + signs[1]
        while 0 <= temp_c < 8 and 0 <= temp_r < 8:
            if chess_board[temp_r][temp_c] == "Q":
                queen_coord = [temp_r, temp_c]
                queens_can_capture.append(queen_coord)
                break
            temp_r += signs[0]
            temp_c += signs[1]
        signs = signs[2:]
    return queens_can_capture


def printer(queens_can_capture):
    if queens_can_capture:
        for queen in queens_can_capture:
            print(queen)
    else:
        print("The king is safe!")


queens_can_capture = []
chess_board = board_creator()
k_row, k_col = king_place(chess_board)
queens_can_capture = row_checker(chess_board, k_row, k_col, queens_can_capture)
queens_can_capture = col_checker(chess_board, k_row, k_col, queens_can_capture)
signs = [1, 1, 1, -1, -1, 1, -1, -1]
diagonals_checker(chess_board, k_row, k_col, signs, queens_can_capture)
printer(queens_can_capture)