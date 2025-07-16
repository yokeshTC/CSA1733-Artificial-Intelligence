import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def alphabeta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = alphabeta(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O")

    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Cell taken. Try again.")
            continue
        board[row][col] = "X"

        if check_winner(board) or is_full(board):
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI moved at:", ai_row, ai_col)

    print_board(board)
    winner = check_winner(board)
    if winner:
        print("Winner is", winner)
    else:
        print("It's a tie")

if __name__ == "__main__":
    main()
