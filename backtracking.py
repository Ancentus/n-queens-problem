def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at position (row, col).
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens_util(board, col, n):
    """
    Utility function to solve n-queens problem recursively.
    """
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            if solve_nqueens_util(board, col + 1, n):
                return True
            board[i][col] = '.'

    return False

def solve_nqueens(n):
    """
    Solve the n-queens problem using backtracking.
    """
    board = [['.' for _ in range(n)] for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist")
        return False

    return board

def display_board(board):
    """
    Display the board with queens placed.
    """
    for row in board:
        print(" ".join(row))
    print()

if __name__ == "__main__":
    n = 8  # Number of queens
    solution = solve_nqueens(n)
    if solution:
        print("Solution:")
        display_board(solution)
