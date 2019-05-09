'''
Othello class with a board member variable that is an 8 X 8 matrix
'''
import ColorPrinter as cp
import random
import sys
W = 'W'
B = 'B'


class OthelloBoard:

    def __init__(self):
        #self.board = [[None for i in range(0, 8)] for i in range(0, 8)]
        self.board = self.debug_board_one()
        self.recent_board = [[None for i in range(0, 8)] for i in range(0, 8)]
        self._reset_highlights()
        self.init_type = self.choose_init_type()
        self.set_init_board(self.init_type)

    def debug_board_one(self):
        b =[[None for i in range(0,8)],
            [None for i in range(0,8)],
            [None, W, W, None, W, None, None, W],
            [None, W, W, B, B, W, W, None],
            [W, W, W, W, W, B, W, W],
            [None, W, W, W, W, W, W, W],
            [None, W, W, W, W, W, W, B],
            [None for i in range(0,8)]]
        return b

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
        return self.get_points_test_board(self.board)

    def get_points_test_board(self, board):
        points_w = 0
        points_b = 0
        for row in board:
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
        if not self._does_board_coord_exist(self.board, cur_r, cur_c) or self.board[cur_r][cur_c] == None:
            return False

        if self.board[cur_r][cur_c] == my_tkn:
            return True

        # if valid move
        if self._make_move_traverse(my_tkn, other_tkn, cur_r + move_r, cur_c + move_c, move_r, move_c):
            # flip tokens while backtracking
            self.board[cur_r][cur_c] = my_tkn
            return True

        return False

    def test_move(self, board, token, row, col):
        next_board = self.clone_test_board(board)
        next_board[row][col] = token
        other_token = B if token == W else W

        # up
        self._test_move_traverse(next_board, token, other_token, row-1, col, -1, 0)
        # up right
        self._test_move_traverse(next_board, token, other_token, row-1, col+1, -1, 1)
        # right
        self._test_move_traverse(next_board, token, other_token, row, col+1, 0, 1)
        # down right
        self._test_move_traverse(next_board, token, other_token, row+1, col+1, 1, 1)
        # down
        self._test_move_traverse(next_board, token, other_token, row+1, col, 1, 0)
        # down left
        self._test_move_traverse(next_board, token, other_token, row+1, col-1, 1, -1)
        # left
        self._test_move_traverse(next_board, token, other_token, row, col-1, 0, -1)
        # up left
        self._test_move_traverse(next_board, token, other_token, row-1, col-1, -1, -1)

        return next_board

    def _test_move_traverse(self, next_board, my_tkn, other_tkn, cur_r, cur_c, move_r, move_c):
        if not self._does_board_coord_exist(next_board, cur_r, cur_c) or next_board[cur_r][cur_c] == None:
            return False

        elif next_board[cur_r][cur_c] == my_tkn:
            return True

        # if valid move
        elif self._test_move_traverse(next_board, my_tkn, other_tkn, cur_r + move_r, cur_c + move_c, move_r, move_c):
            # flip tokens while backtracking
            next_board[cur_r][cur_c] = my_tkn
            return True
        else:
            return False

    def _does_board_coord_exist(self, board, r, c):
        if 0 <= r and r < len(board[0]):
            if 0 <= c and c < len(board):
                return True 
        return False

    def clone_test_board(self, board):
        new = [[None for i in range(0, 8)] for i in range(0, 8)]
        for idx, row in enumerate(board):
            new[idx] = row.copy()

        return new

    def highlight_move(self, token, row, col):
        self._reset_highlights()

        row = row - 1
        col = ord(col) - ord('A')

        newb = self._clone_board()
        newb[row][col] = token

        self.highlights[row][col] = True
        other_token = B if token == W else W

        # up
        self._highlight_move_traverse(
            newb, token, other_token, row-1, col, -1, 0)
        # up right
        self._highlight_move_traverse(
            newb, token, other_token, row-1, col+1, -1, 1)
        # right
        self._highlight_move_traverse(
            newb, token, other_token, row, col+1, 0, 1)
        # down right
        self._highlight_move_traverse(
            newb, token, other_token, row+1, col+1, 1, 1)
        # down
        self._highlight_move_traverse(
            newb, token, other_token, row+1, col, 1, 0)
        # down left
        self._highlight_move_traverse(
            newb, token, other_token, row+1, col-1, 1, -1)
        # left
        self._highlight_move_traverse(
            newb, token, other_token, row, col-1, 0, -1)
        # up left
        self._highlight_move_traverse(
            newb, token, other_token, row-1, col-1, -1, -1)

        self._draw_board(newb, should_highlight=True)

    def _highlight_move_traverse(self, board, my_token, other_token, cur_r, cur_c, move_r, move_c):
        if not self._does_board_coord_exist(board, cur_r, cur_c) or board[cur_r][cur_c] == None:
            return False

        if board[cur_r][cur_c] == my_token:
            return True

        # if valid move
        if self._highlight_move_traverse(board, my_token, other_token, cur_r + move_r, cur_c + move_c, move_r, move_c):
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

    def choose_init_type(self):
        initial = input(
            "Please enter 1 if you would like the board to begin with WB, else enter 0 if you would like the board to be BW: ")
        print("initial: ", initial)
        if initial == 'QUIT':
            print('Goodbye.')
            sys.exit(0)

        while type(initial) is str:
            try:
                initial = int(initial)
            except:
                print("Invalid selection. Must have the form <Board number>. ")
                initial = input("Please re enter your selection: ")

        return initial

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
        return self.check_valid_move_test_board(self.board, move_row, move_column, player_color)

    def check_valid_move2(self, move_row, move_column, player_color):
        move_column = ord(move_column) - ord('A')
        move_row = int(move_row) - 1
        return self.check_valid_move_test_board2(self.board, move_row, move_column, player_color)

    def check_valid_move_test_board(self, board, move_row, move_column, player_color):

        if type(move_column) is str:
            move_column = ord(move_column) - ord('A')
            move_row = int(move_row) - 1

        legal_move = False
        if board[move_row][move_column] is None:
            # if there is nothing in that spot, then the move may be legal
            # go in all eight dirrections
            #   keep going in that direction so long as token but not your token
            #       if your token, valid move
            found_same_color = False
            xposition = move_column
            yposition = move_row
            current_color = board[yposition][xposition]
            for column in range(-1, 2):
                if legal_move is True:
                    break
                for row in range(-1, 2):
                    xposition = move_column + column
                    yposition = move_row + row
                    if xposition < (len(board)) and yposition < (len(board)):
                        current_color = board[yposition][xposition]
                    else:
                        continue
                    # if current_color is empty, the player_color or out of bounds, then check in a different direction
                    if (current_color is player_color) or (current_color is None):
                        # don't want to break out of the loop, else directions may be skipped
                        continue
                    while found_same_color is False and xposition < (len(board) - 1) and xposition >= 0 and yposition < (len(board) - 1) and yposition >= 0:
                        # continue checking in that direction
                        xposition += column
                        yposition += row

                        current_color = board[yposition][xposition]
                        if current_color is player_color:
                            found_same_color = True
                            legal_move = True
                            break
                        if current_color is -1:
                            break

        return legal_move

    def check_valid_move_test_board2(self, board, row, col, token):
        if board[row][col] != None:
            return False

        other_token = B if token == W else W

        # up
        if self.check_valid_move_test_board2_traverse(False, board, token, other_token, row-1, col, -1, 0):
            return True
        # up right
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row-1, col+1, -1, 1):
            return True
        # right
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row, col+1, 0, 1):
            return True
        # down right
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row+1, col+1, 1, 1):
            return True
        # down
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row+1, col, 1, 0):
            return True
        # down left
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row+1, col-1, 1, -1):
            return True
        # left
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row, col-1, 0, -1):
            return True
        # up left
        elif self.check_valid_move_test_board2_traverse(False, board, token, other_token, row-1, col-1, -1, -1):
            return True
        else:
            return False
    
    def check_valid_move_test_board2_traverse(self, has_other_token, board, my_token, other_token, cur_r, cur_c, move_r, move_c):
        if not self._does_board_coord_exist(board, cur_r, cur_c) or board[cur_r][cur_c] == None:
            return False

        elif board[cur_r][cur_c] == my_token and has_other_token:
            return True

        elif board[cur_r][cur_c] == my_token and not has_other_token:
            return False

        elif board[cur_r][cur_c] == other_token:
            has_other_token = True
            return self.check_valid_move_test_board2_traverse(True, board, my_token, other_token, cur_r + move_r, cur_c + move_c, move_r, move_c)

        
        else:
            print('Malformed token at ' + str(cur_r) + ', ' + str(cur_c) + ': ' + board[cur_r][cur_c])
            return False
    
    def has_move(self, token):
        return self.has_move_test_board(self.board, token)

    def has_move_test_board(self, board, token):
        row_index = 0
        for row in board:
            column_index = 0
            for column in row:
                move_row = row_index
                move_column = column_index
                if self.check_valid_move_test_board(board, move_row, move_column, token):
                    return True
                column_index += 1
            row_index += 1
        return False

    def convert_to_real_coords(self, move):
        c = chr(ord('A') + move[1])
        r = move[0] + 1
        return r, c

    '''
    Finds all current possible moves 
    Returns valid_moves: contains tuples of each possible move
    '''

    def get_possible_moves(self, board, token):
        valid_moves = []
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                move_row, move_col = self.convert_to_real_coords((row_idx, col_idx))
                if self.check_valid_move2(move_row, move_col, token):
                    valid_moves.append((row_idx, col_idx))
                
        return valid_moves
