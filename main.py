'''
Class: CPSC 427
Team Member 1: Kathrine Gibson
Team Member 2: Kasey Davis
Submitted By Kathrine Gibson
GU Username: kgibson2
File Name: main.py
Creates the interface for a game of Othello

Usage 1:  python3 <program name>
          python3 main.py
'''
import othello_board
import ColorPrinter as cp


def main():
    new_board = othello_board.OthelloBoard()
    new_board.draw_board()
    get_move()


def get_move():
    move = input("Choose position (R C): ")
    is_length_three = is_col_valid = is_row_valid = False

    is_length_three = len(move) == 3

    if is_length_three:
        is_col_valid = ord(move[2]) in range(ord('A'), ord('I'))
        is_row_valid = ord(move[0]) in range(ord('1'),ord('9'))

    while not is_length_three or not is_col_valid or not is_row_valid:
        print("Invalid selection. Must have the form <Row number> <Column char>.")
        move = input("Choose position (R C): ")

        is_length_three = len(move) == 3

        if is_length_three:
            is_col_valid = ord(move[2]) in range(ord('A'), ord('I'))
            is_row_valid = ord(move[0]) in range(ord('1'),ord('9'))

    return (move[0], move[2])

def format_move(pair):
    return (int(pair[0]), pair[1])

if __name__ == "__main__":
    main()
