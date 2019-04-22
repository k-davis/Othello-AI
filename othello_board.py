'''
Othello class with a board member variable that is an 8 X 8 matrix
'''


class OthelloBoard:
    W = 'W'
    B = 'B'

    def __init__(self):
        row = [None for i in range(0, 8)]
        self.board = [row for i in range(0, 8)]

    def set_init_board(self, board_type):
        # if board_type 1, then WB, else BW
        if board_type is 1:
            self.board[3][3] = W
            self.board[3][4] = B
            self.board[4][3] = B
            self.board[4][4] = W
        else:
            self.board[3][3] = B
            self.board[3][4] = W
            self.board[4][3] = W
            self.board[4][4] = B
