import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board, player):
    win_positions = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    for positions in win_positions:
        if all(board[r][c] == player for r, c in positions):
            return True
    return False

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"\nPlayer {player}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"\nPlayer {player} wins!")
                break
            elif all(board[r][c] != " " for r in range(3) for c in range(3)):
                print_board(board)
                print("\nIt's a draw!")
                break
            turn += 1
        else:
            print("\nInvalid move. Try again.")

# Example usage:
print("\nLet's play Tic-Tac-Toe!")
play_tic_tac_toe()