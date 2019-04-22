'''
Othello class with a board member variable that is an 8 X 8 matrix
'''
import ColorPrinter as cp
import random
W = 'W'
B = 'B'
class OthelloBoard:
    

    def __init__(self):
        row = [None for i in range(0, 8)]
        self.board = [row for i in range(0, 8)]
        self.rand_board()
        self.draw_board()

    def rand_board(self):
        tkns = [None, B, W]
        self.board = [[tkns[random.randint(0,2)] for i in range(0,8)] for i in range (0,8)]
        
                
    
    def draw_board(self):
        for row in self.board:
            for token in row:
                
                if token == None:
                    self.draw_blank()
                elif token == W:
                    self.draw_w()
                elif token == B:
                    self.draw_b()
            print()

    def draw_w(self):
        cp.cprint(cp.BK_DK_GREEN, cp.F_WHITE, W + ' ')

    def draw_b(self):
        cp.cprint(cp.BK_DK_GREEN, cp.F_BLACK, B + ' ')

    def draw_blank(self):
        cp.cprint(cp.BK_DK_GREEN, cp.F_BLACK, '  ')


