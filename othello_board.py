'''
Othello class with a board member variable that is an 8 X 8 matrix
'''
import ColorPrinter as cp
import random
W = 'W'
B = 'B'


class OthelloBoard:

    def __init__(self):
        self.board = [[None for i in range(0, 8)] for i in range(0, 8)]
        self.set_init_board(1)

    def rand_board(self):
        tkns = [None, B, W]
        self.board = [[tkns[random.randint(0, 2)]
                       for i in range(0, 8)] for i in range(0, 8)]

    def draw_board(self):
        # print board column headers
        print(' ', end='')
        col_hdrs = [print(chr(e) + ' ', end='') for e in range(ord('A'), ord('I'))]
        print()

        for r_idx, row in enumerate(self.board):
            print(r_idx + 1, end='')

            for token in row:
                if token == None:
                    self.draw_blank()
                elif token == W:
                    self.draw_w()
                elif token == B:
                    self.draw_b()
            print()

    def make_a_move(self, token, row, col):
        row = row - 1
        col = ord(col) - ord('A')
        self.board[row][col] = token

        other_token = B if token == W else W

        # up
        self._make_move_traverse(token, other_token, row-1, col, -1, 0)
        # up right
        self._make_move_traverse(token, other_token, row-1, col+1, -1, 1)
        # right
        self._make_move_traverse(token, other_token, row, col+1, 0, 1)
        # down right
        self._make_move_traverse(token, other_token, row+1, col+1, 1, 1)
        # down
        self._make_move_traverse(token, other_token, row+1, col, 1, 0)
        # down left
        self._make_move_traverse(token, other_token, row+1, col-1, 1, -1)
        # left
        self._make_move_traverse(token, other_token, row, col-1, 0, -1)
        # up left
        self._make_move_traverse(token, other_token, row-1, col-1, -1, -1)

        self.draw_board()
        

    def _make_move_traverse(self, my_tkn, other_tkn, cur_r, cur_c, move_r, move_c):
        if self.board[cur_r][cur_c] == None:
            return False

        if self.board[cur_r][cur_c] == my_tkn:
            return True
        
        # if valid move
        if self._make_move_traverse(my_tkn, other_tkn, cur_r + move_r, cur_c + move_c, move_r, move_c):
            # flip tokens while backtracking
            self.board[cur_r][cur_c] = my_tkn
            return True

        return False


    def draw_w(self):
        cp.cprint(cp.BK_DK_RED, cp.F_WHITE, W + ' ')

    def draw_b(self):
        cp.cprint(cp.BK_DK_RED, cp.F_BLACK, B + ' ')

    def draw_blank(self):
        cp.cprint(cp.BK_DK_RED, cp.F_BLACK, '  ')

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
