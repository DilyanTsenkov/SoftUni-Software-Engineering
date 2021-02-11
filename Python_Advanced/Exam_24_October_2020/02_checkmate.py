def board_creator():
    chess_board = [input().split() for _ in range(8)]
    return chess_board


def king_place(chess_board):
    for row in range(8):
        if "K" in chess_board[row]:
            col = chess_board[row].index("K")
            break
    return row, col


def queens_finder(chess_board, k_row, k_col, queens_can_capture):
    signs = [1, 1, 1, -1, -1, 1, -1, -1, 1, 0, 0, 1, -1, 0, 0, -1]
    for _ in range(8):
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


chess_board = board_creator()
k_row, k_col = king_place(chess_board)
queens_can_capture = []
queens_finder(chess_board, k_row, k_col, queens_can_capture)
printer(queens_can_capture)