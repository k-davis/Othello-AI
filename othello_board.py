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
        self.recent_board = [[None for i in range(0, 8)] for i in range(0, 8)]
        self._reset_highlights()
        self.set_init_board(1)

    def rand_board(self):
        tkns = [None, B, W]
        self.board = [[tkns[random.randint(0, 2)]
                       for i in range(0, 8)] for i in range(0, 8)]

    def _draw_board(self, board, should_highlight=False):
        # print board column headers
        print(' ', end='')
        col_hdrs = [print(chr(e) + ' ', end='')
                    for e in range(ord('A'), ord('I'))]
        print()

        for r_idx, row in enumerate(board):
            print(r_idx + 1, end='')

            for c_idx, token in enumerate(row):
                if token == None:
                    self._draw_blank()
                elif token == W:
                    self._draw_w(self.highlights[r_idx][c_idx])
                elif token == B:
                    self._draw_b(self.highlights[r_idx][c_idx])
            print()

    def show_move(self, token, row, col):
        new = self._clone_board()
        self._reset_highlights()
        row -= 1
        col = ord(col) - ord('A')
        new[row][col] = token 
        self.highlights[row][col] = True

        self._draw_board(new, should_highlight=False)


    def draw(self):
        self._reset_highlights()
        self._draw_board(self.board)

    def _reset_highlights(self):
        self.highlights = [[False for i in range(0, 8)] for i in range(0, 8)]

    def get_points(self):
        points_w = 0
        points_b = 0
        for row in self.board:
            for elem in row:
                if elem == W:
                    points_w += 1
                elif elem == B:
                    points_b += 1
        return points_b, points_w

    def make_move(self, token, row, col):
        self.save_board()
        self._reset_highlights()

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

    def highlight_move(self, token, row, col):
        self._reset_highlights()

        row = row - 1
        col = ord(col) - ord('A')

        newb = self._clone_board()
        newb[row][col] = token

        self.highlights[row][col] = True
        other_token = B if token == W else W

        # up
        self._highlight_move_traverse(newb, token, other_token, row-1, col, -1, 0)
        # up right
        self._highlight_move_traverse(newb, token, other_token, row-1, col+1, -1, 1)
        # right
        self._highlight_move_traverse(newb, token, other_token, row, col+1, 0, 1)
        # down right
        self._highlight_move_traverse(newb, token, other_token, row+1, col+1, 1, 1)
        # down
        self._highlight_move_traverse(newb, token, other_token, row+1, col, 1, 0)
        # down left
        self._highlight_move_traverse(newb, token, other_token, row+1, col-1, 1, -1)
        # left
        self._highlight_move_traverse(newb, token, other_token, row, col-1, 0, -1)
        # up left
        self._highlight_move_traverse(newb, token, other_token, row-1, col-1, -1, -1)

        self._draw_board(newb, should_highlight=True)

    def _highlight_move_traverse(self, board, my_token, other_token, cur_r, cur_c, move_r, move_c):
        if board[cur_r][cur_c] == None:
            return False

        if board[cur_r][cur_c] == my_token:
            return True

        # if valid move
        if self._make_move_traverse(my_token, other_token, cur_r + move_r, cur_c + move_c, move_r, move_c):
            # flip tokens while backtracking
            self.highlights[cur_r][cur_c] = True
            return True

        return False

    def save_board(self):
        for idx, row in enumerate(self.board):
            self.recent_board[idx] = row.copy()

    def _clone_board(self):
        new = [[None for i in range(0, 8)] for i in range(0, 8)]

        for idx, row in enumerate(self.board):
            new[idx] = row.copy()

        return new

    def draw_previous_board(self):
        self._draw_board(self.recent_board)

    def revert(self):
        self.board = self.recent_board
        self._reset_highlights()

    def _draw_w(self, should_highlight):
        if should_highlight:
            cp.cprint(cp.BK_RED, cp.F_WHITE, W + ' ')
        else:
            cp.cprint(cp.BK_DK_RED, cp.F_WHITE, W + ' ')

    def _draw_b(self, should_highlight):
        if should_highlight:
            cp.cprint(cp.BK_RED, cp.F_BLACK, B + ' ')
        else:
            cp.cprint(cp.BK_DK_RED, cp.F_BLACK, B + ' ')

    def _draw_blank(self):
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

    def check_valid_move(self, move_row, move_column, player_color):

        if type(move_column) is str:
            move_column = ord(move_column) - ord('A')
            move_row = int(move_row) - 1

        legal_move = False
        if self.board[move_row][move_column] is None:
            # if there is nothing in that spot, then the move may be legal
            # go in all eight dirrections
            #   keep going in that direction so long as token but not your token
            #       if your token, valid move
            found_same_color = False
            xposition = move_column
            yposition = move_row
            current_color = self.board[yposition][xposition]
            for column in range(-1, 2):
                if legal_move is True:
                    break
                for row in range(-1, 2):
                    xposition = move_column + column
                    yposition = move_row + row
                    if xposition < (len(self.board) - 1) and yposition < (len(self.board) - 1):
                        current_color = self.board[yposition][xposition]
                    else:
                        continue
                    # if current_color is empty, the player_color or out of bounds, then check in a different direction
                    if (current_color is player_color) or (current_color is None):
                        # don't want to break out of the loop, else directions may be skipped
                        continue
                    while found_same_color is False and xposition < (len(self.board) - 1) and xposition >= 0 and yposition < (len(self.board) - 1) and yposition >= 0:
                        # continue checking in that direction
                        xposition += column
                        yposition += row
                        
                        current_color = self.board[yposition][xposition]
                        if current_color is player_color:
                            found_same_color = True
                            legal_move = True
                            break
                        if current_color is -1:
                            break

        return legal_move

    def has_move(self, token):
        row_index = 0
        for row in self.board:
            column_index = 0
            for column in row:
                move_row = row_index
                move_column = column_index
                if self.check_valid_move(move_row, move_column, token):
                    return True
                column_index += 1
            row_index += 1
        return False
