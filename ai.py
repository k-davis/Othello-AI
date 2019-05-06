# constructor which takes a token type
# make a move function, takes in current board
# black is max
# white is min
# score is b - w
MAX_TIME = 10
DEPTH_LIMIT = 5
INF = float('inf')
NEG_INF = float('-inf')
W = 'W'
B = 'B'

class AI:
    def __init__(self, token, oth):
        self.token = token
        self.oth = oth

    def make_a_move(self, board):
        should_max = (self.token == B)
        alpha = Node(NEG_INF)
        alpha.board = board 
        beta = Node(INF)
        beta.board = board
        node = self.minimax(0, 0, should_max, alpha, beta)
        return node.move


    def minimax(self, depth, pnode, is_max, alpha, beta):
        tkn = self.token_from(is_max)
        if self.oth.has_move_test_board(pnode.board, tkn) or depth == DEPTH_LIMIT:
            return node

        if is_max:
            best_node = Node(NEG_INF)
            for move in self.oth.get_possible_moves(pnode.board, token):
                cnode = Node(pnode.board, move)
                next_node = self.minimax(cnode, depth+1, false, alpha, beta)

                best_node = self.max_node(best_node, next_node)
                alpha = self.max_node(alpha, best_node)

                if beta.score <= alpha.score:
                    break
            return best_node
        
        else:
            best_node = Node(INF) 
            for move in self.oth.get_possible_moves(pnode.board,token):
                cnode = Node(pnode.board, move)

                next_node = minimax(cnode, depth+1, true, alpha, beta)
                best_node = self.min_node(best_node, next_node)
                beta = self.min_node(beta, best_node)

                if beta.score <= alpha.score:
                    break

            return best_node

    def token_from(self, is_max):
        return B if is_max else W

    def max_node(self, a, b):
        if a.score < b.score:
            return b
        else:
            return a

    def min_node(self, a, b):
        if b.score < a.score:
            return b
        else:
            return a

class Node:
    def __init__(self, old_board, move, oth):
        self.board = oth.test_move(oth.clone_test_board(old_board), token, move[0], move[1])
        self.move = move
        b, w = oth.get_points_test_board(self.board)
        self.score = b - w

    def __init__(self, score):
        self.score = score