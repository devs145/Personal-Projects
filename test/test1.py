import random

# Board initialization
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Function to display the Tic Tac Toe board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the game is over
def game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True

    if board[2] == board[4] == board[6] and board[2] != " ":
        return True

    # Check if the board is full
    if " " not in board:
        return True

    # If none of the above conditions are true, the game is not over
    return False

# Function for the AI's move
def ai_move():
    global board
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            break

# Function for the player's move
def player_move():
    global board
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break

# Function to play the game
def play_game():
    display_board()
    while not game_over():
        player_move()
        display_board()
        if game_over():
            break
        print("AI's turn...")
        ai_move()
        display_board()

    # Game over message
    if " " not in board:
        print("The game is tied!")
    elif board.count("X") > board.count("O"):
        print("You won!")
    else:
        print("You lost!")

# Start the game
play_game()
