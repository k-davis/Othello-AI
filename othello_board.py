'''
Othello class with a board member variable that is an 8 X 8 matrix
'''


class OthelloBoard:

    def __init__(self):
        row = [None for i in range(0, 8)]
        self.board = [row for i in range(0, 8)]
