# Tic-Tac-Toe game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return " " not in board

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    # Initialize an empty board
    board = [" "] * 9
    current_player = "X"  # X always goes first
    
    # Loop until there is a win or a tie
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Take input and validate it
        while True:
            try:
                move = int(input(f"Choose a position (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("This position is already taken. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number between 1 and 9.")
        
        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
