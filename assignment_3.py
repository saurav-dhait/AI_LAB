def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions

# Example usage for 8-Queens problem:
n = 8
solutions = solve_n_queens(n)
print(f"\nSolutions for {n}-Queens problem:")
for solution in solutions:
    print(solution)