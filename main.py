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


class OthelloAI:
    def __init__(self):
        self.board = othello_board.OthelloBoard()
        self.my_token = self.get_my_color()
        self.board.draw()

    def get_move(self):
        move = input("Choose position (R C): ")
        is_length_three = is_col_valid = is_row_valid = False

        is_length_three = len(move) == 3

        if is_length_three:
            is_col_valid = ord(move[2]) in range(ord('A'), ord('I'))
            is_row_valid = ord(move[0]) in range(ord('1'), ord('9'))

        while not is_length_three or not is_col_valid or not is_row_valid:
            print("Invalid selection. Must have the form <Row number> <Column char>.")
            move = input("Choose position (R C): ")

            is_length_three = len(move) == 3

            if is_length_three:
                is_col_valid = ord(move[2]) in range(ord('A'), ord('I'))
                is_row_valid = ord(move[0]) in range(ord('1'), ord('9'))

        return (int(move[0]), move[2])

    def get_my_color(self):
        color = input('Will you play as black (B) or white (W)? ')

        while color not in ['B', 'W']:
            print('Selection must be either \'B\' or \'W\'')
            color = input('Will you play as black (B) or white (W)? ')

        return color

    def display_score(self):
        score = self.new_board.get_points()
        print('  -- Score --')
        print(' Black: ' + str(score[0]))
        print(' White: ' + str(score[1]))


if __name__ == "__main__":
    AI = OthelloAI()
    won = False
    while(won is False):
        row, column = OthelloAI.get_move()
        row = int(row)
        column = ord(column) - 65
        print(column)
        if AI.board.check_valid_move(row, column, AI.my_token):
            print("valid")
