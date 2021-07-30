"""
BOARD REPRESENTATION
    7|8|9
    -----
    4|5|6
    -----
    1|2|3
"""

import random


PLAYERS = ['X', 'O']

def get_new_board():
    return [' '] * 10

def print_board(b):
    # Parameter 'b' -> board
    print(b[7] + '|' + b[8] + '|' + b[9])
    print("- - -")
    print(b[4] + '|' + b[5] + '|' + b[6])
    print("- - -")
    print(b[1] + '|' + b[2] + '|' + b[3])

def get_turn(playing):
    if playing == PLAYERS[0]:
        return PLAYERS[1]
    return PLAYERS[0]

def check_win(b, p):
    return (b[7] == b[8] == b[9] == p) or\
           (b[4] == b[5] == b[6] == p) or\
           (b[1] == b[2] == b[3] == p) or\
           (b[7] == b[4] == b[1] == p) or\
           (b[8] == b[5] == b[2] == p) or\
           (b[9] == b[6] == b[3] == p) or\
           (b[7] == b[5] == b[3] == p) or\
           (b[9] == b[5] == b[1] == p)

def who_plays_first():
    p1 = random.choice(PLAYERS)
    p2 = PLAYERS[0] if p1 != PLAYERS[0] else PLAYERS[1]
    print("Player 1 is", p1)
    print("Player 2 is", p2)
    return p1, p2, random.choice([p1, p2])

def get_valid_user_move():
    move = ''
    while str(move) not in '1 2 3 4 5 6 7 8 9'.split():
        move = int(input("Enter your position (1-9):"))
    return move

def can_make_move(board, move):
    if move == 0:
        return False
    return board[move] == ' '

def make_move(board, move, player):
    board[move] = player


def main():
    board = get_new_board()
    player1, player2, playing = who_plays_first()
    while True:
        print_board(board)
        print(f"Its your turn Player {playing}")
        move = get_valid_user_move()
        if playing == player1:
            if can_make_move(board, move):
                make_move(board, move, playing)
                if check_win(board, playing):
                    print("Player", playing, "wins")
                    break
                playing = player2                    
        else:
            if can_make_move(board, move):
                make_move(board, move, playing)
                if check_win(board, playing):
                    print("Player", playing, "wins")
                    break
                playing = player1

        if ' ' not in board[1:]:
            print("Its a tie. Nobody wins")
            break
        
    print_board(board)

main()
