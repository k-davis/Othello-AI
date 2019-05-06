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
import time
import sys
import ai
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

        while(self.board.has_move(W) and self.board.has_move(B)):
            if self.next_player == self.my_token:
                self.do_human_turn()
            elif self.next_player == self.ai_token:
                self.do_ai_turn()
            else:
                print("Oh shoot, this isn't good")
                sys.exit(0)

            if self.next_player == B:
                self.next_player = W
            else:
                self.next_player = B

    def do_ai_turn(self):
        inp = input('AI: Ready to make a move... (enter to continue) ')
        if inp == 'QUIT':
            sys.exit(0)
        elif inp == 'REVERT':
            self.revert()
        else:
            print('Timer has begun. 10 seconds.')
            print()

            start_time = time.time()

            print('** For demonstration purposes choose for the AI **')
            move = self.get_move()

            if move == 'REVERT':
                self.revert()
            else:
                while not self.board.check_valid_move(move[0], move[1], self.ai_token):
                    print('That is an invalid move. Try again.')
                    move = self.get_move()

                print_gap()

                self.board.highlight_move(self.ai_token, move[0], move[1])
                print('Here is my move (' +
                      str(move[0]) + ', ' + str(move[1]) + ')')

                elapsed_time = time.time() - start_time
                print('AI thinking time elapsed: ' + str(elapsed_time))
                if elapsed_time > 10:
                    print(
                        'The AI has taken too long! ... but will not lose for the demo')

                input('Confirm? ')
                print()

                self.board.make_move(self.ai_token, move[0], move[1])
                self.board.draw()
                self.display_score()
                print()

    def do_human_turn(self):
        move = self.get_move()

        if move == 'REVERT':
            self.revert()
        else:

            while not self.board.check_valid_move(move[0], move[1], self.my_token):
                print('That is an invalid move. Try again.')
                move = self.get_move()

            self.board.highlight_move(self.my_token, move[0], move[1])
            print()

            confirmation = input('Confirm? (Y/N): ')
            while confirmation not in ['Y', 'N']:
                print('Invalid response. Try again.')
                confirmation = input('Confirm? (Y/N)')

            print()

            if confirmation == 'Y':
                self.board.make_move(self.my_token, move[0], move[1])
                self.board.draw()
                self.display_score()
            else:
                self.board.draw()
                self.do_human_turn()
            print()

    def get_move(self):
        move = input("Choose position (R C): ")

        if move == 'QUIT':
            print('Goodbye.')
            sys.exit(0)
        if move == 'REVERT':
            return move

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
        print('Reverting to previous state...')
        print()
        self.board.revert()
        self.board.draw()
        print()

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


def print_gap():
    print('\n\n\n\n')


if __name__ == "__main__":
    OthelloProg()
