from decimal import Decimal, ROUND_HALF_UP

SIZE = 8
chess_board = [[sq for sq in input().split()] for row in range(SIZE)]

# position of each pawn as a list with indexes
position_w = []
position_b = []

for row in range(SIZE):
    for col in range(SIZE):
        current_sq = chess_board[row][col]
        if current_sq == "w":
            position_w.append(row)
            position_w.append(chess_board[row].index("w"))
        if current_sq == "b":
            position_b.append(row)
            position_b.append(chess_board[row].index("b"))


nearby = abs(position_w[1] - position_b[1])  # if both pawns are nearby

# the real chess position of the pawns
chess_row_w = SIZE - position_w[0]
chess_col_w = chr(97 + position_w[1])
chess_row_b = SIZE - position_b[0]
chess_col_b = chr(97 + position_b[1])


if nearby != 1 or chess_row_w >= chess_row_b:
    sq_left_for_w = position_w[0]
    sq_left_for_b = SIZE - 1 - position_b[0]

    if sq_left_for_w > sq_left_for_b:
        print(f"Game over! Black pawn is promoted to a queen at {chess_col_b}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chess_col_w}8.")
else:
    diff = abs(position_w[0] - position_b[0])
    rounded_diff = Decimal(diff/2).quantize(0, ROUND_HALF_UP)
    if diff % 2 != 0:
        print(f"Game over! White win, capture on {chess_col_b}{chess_row_b - rounded_diff+1}.")
    else:
        print(f"Game over! Black win, capture on {chess_col_w}{chess_row_w + rounded_diff}.")
