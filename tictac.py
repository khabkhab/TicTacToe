import random
from tkinter.tix import InputOnly
#initial variables 
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = ["-" for x in range(9)]

separator = "+---+---+---+"
Player = "X"


winner = None
game_running = True

#print game board function
def print_board(game_board):
    print(separator)
    print("| " + game_board[0]+ " | " + game_board[1]+ " | " + game_board[2]+ " |")
    print(separator)
    print("| " + game_board[3]+ " | " + game_board[4]+ " | " + game_board[5]+ " |")
    print(separator)
    print("| " + game_board[6]+ " | " + game_board[7]+ " | " + game_board[8]+ " |")
    print(separator)
    
#function that receives input from players
def players_input(game_board):
    input_1 = int(input("Choose the spot from [1-9]: "))
    if input_1 >= 1 and input_1 <= 9 and game_board[input_1-1] == "-":
        game_board[input_1-1] = Player
    else:
        print("Spot is occupied. Cannot you see?")

#check for the winner
def check_row(game_board):
    global winner 
    if game_board[0] == game_board[1] == game_board[2] and game_board[1] != "-":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[4] != "-":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[7] != "-":
        winner = game_board[6]
        return True
def check_col(game_board):
    global winner 
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        winner = game_board[2]
        return True
def check_diag(game_board):
    global winner 
    if game_board[0] == game_board[4] == game_board[8] and game_board[4] != "-":
        winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[4] != "-":
        winner = game_board[2]
        return True

#checking if it is a tie
def check_tie(game_board):
    global game_running
    if "-" not in game_board:
        print_board(game_board)
        print("It is a tie")
        game_running = False
        
def winner_check():
    global game_running
    if check_col(game_board) or check_diag(game_board) or check_row(game_board):
        print(f"The Winner is {winner}")
        print_board(game_board)
        game_running = False
        
#introducing second player
def change_player():
    global Player 
    if Player == "X":
        Player = "O"
    else:
        Player = "X"
def CPU(game_board):
    while Player == "O":
        guess = random.randint(0, 8)
        if game_board[guess] == "-":
            game_board[guess] = "O"
            change_player()
decision = input("If you want to playe with computer, type yes: ").lower()
if decision == "yes":
    while game_running:      
        print_board(game_board)
        players_input(game_board)
        winner_check()
        check_tie(game_board)
        change_player()
        CPU(game_board)
        winner_check()
        check_tie(game_board)
else:
    while game_running:
        print_board(game_board)
        players_input(game_board)
        winner_check()
        check_tie(game_board)
        change_player()