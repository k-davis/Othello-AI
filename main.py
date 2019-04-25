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

B = 'B'
W = 'W'

class OthelloProg:
    def __init__(self):
        self.board = othello_board.OthelloBoard()

        print()
        self.board.draw()
        self.display_score()
        print()

        self.my_token = self.get_my_color()
        print()

        self.ai_token = B if self.my_token == W else W
        
        self.next_player = B

        self.do_ai_turn()
        
        
        '''
        won = False
        while(won is False):
            row, column = self.get_move()
            print(str(row) + ', ' + str(column))
            if self.board.check_valid_move(row, column, self.my_token):
                print("valid")
        '''

    def do_ai_turn(self):
        input('Ready to make a move... (enter to continue)')

        print()
        print('Here is my move (x, x)')

        print('** For demonstration purposes choose for the AI **')
        move = self.get_move()

        while not self.board.check_valid_move(move[0], move[1], self.ai_token):
            print('That is an invalid move. Try again.')
            move = self.get_move()
        print()
        
        self.board.make_move(self.ai_token, move[0], move[1])

        self.board.draw()

        self.display_score()


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

    def revert(self):
        self.board.revert()

    def get_my_color(self):
        color = input('Will you play as black (B) or white (W)? ')

        while color not in [B, W]:
            print('Selection must be either \'B\' or \'W\'')
            color = input('Will you play as black (B) or white (W)? ')

        print('You have chosen: ' + color + '.')

        return color

    def display_score(self):
        score = self.board.get_points()
        print('  -- Score --')
        print(' Black: ' + str(score[0]))
        print(' White: ' + str(score[1]))


if __name__ == "__main__":
    OthelloProg()
    
