import random

MOVES = ['R', 'P', 'S']

def get_player_input():
    move = input("Enter your move (R, P, S)?").upper()
    while move not in MOVES:
        move = input("Enter your move (R, P, S)?").upper()
    return move

def check_winner(p1, p2):
    if (p1 == 'R' and p2 == 'S') or\
       (p1 == 'S' and p2 == 'P') or\
       (p1 == 'P' and p2 == 'R'):
        return True
        

while True:
    print("P for Paper, S for Scissors, and R for Rock")
    player1 = get_player_input()
    print("Player 1:", player1)
    player2 = random.choice(MOVES)
    print("Player 2:", player2)

    if check_winner(player1, player2):
        print("Player 1 wins the game!")
    elif check_winner(player2, player1):
        print("Player 2 wins the game!")
    else:
        print("It's a tie")

    play_again = input("Do you want to play again?").lower()
    if play_again in "yes":
        continue
    else:
        break
