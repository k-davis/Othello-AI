# constructor which takes a token type
# make a move function, takes in current board


class ai:
    def __init__(self, token):
        self.token = token

    def make_a_move(self, board):
        possible_moves = board.get_possible_moves(self.token)
        move = self.alpha_beta_pruning(board, token)

    def alpha_beta_pruning(self, board, token):

        return move
