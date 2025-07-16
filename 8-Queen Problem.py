N = 8
def print_solution(board):
    for row in board:
        line = ""
        for col in row:
            line += "Q " if col else ". "
        print(line)
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row):
    if row == N:
        print_solution(board)
        return True
    found_solution = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                found_solution = True
            board[row][col] = 0  # Backtrack
    return found_solution

# Main
if __name__ == "__main__":
    chess_board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(chess_board, 0):
        print("No solution found.")
