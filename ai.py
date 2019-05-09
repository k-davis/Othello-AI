import time

# constructor which takes a token type
# make a move function, takes in current board
# black is max
# white is min
# score is b - w
MAX_TIME = 10
DEPTH_LIMIT = 4
INF = float('inf')
NEG_INF = float('-inf')
W = 'W'
B = 'B'


class AI:
    def __init__(self, token, oth):
        self.token = token
        self.oth = oth

    def make_a_move(self, board, start_time):
        should_max = (self.token == B)
        alpha = Node(score=NEG_INF, old_board=board, oth=self.oth)
        beta = Node(score=INF, old_board=board, oth=self.oth)
        pnode = Node(old_board=board, oth=self.oth)

        moves = self.oth.get_possible_moves(
            pnode.board, self.token_from(should_max))
        nodes = []

        # calculate the potential value for each possible move
        for move_num, move in enumerate(moves):
            move_node = Node(move=move, oth=self.oth, token=self.token_from(should_max), old_board=pnode.board)
            node_potential = self.minimax(0, move_node, not should_max, alpha, beta)
            nodes.append({'next_move':move, 'potential_score':node_potential.score})

            print(time.time() - start_time)
            if time.time() - start_time > 9:
                print('Time is running out... wrapping up hastily at ' + str(move_num + 1) + '/' + str(len(moves)) + ' child moves measured.')
                break
        
        nodes.sort(key=(lambda e : e['potential_score']))
        
        if should_max:
            best_move = nodes[-1]['next_move']
        else:
            best_move = nodes[0]['next_move']

        print('Moves ' + str(nodes))
        if(best_move == pnode.move):
            print("no move found")
        
        return best_move

    def minimax(self, depth, pnode, is_max, alpha, beta):
        tkn = self.token_from(is_max)
        if not self.oth.has_move_test_board(pnode.board, tkn) or depth == DEPTH_LIMIT:
            return pnode

        if is_max:
            best_node = Node(score=NEG_INF)
            for move in self.oth.get_possible_moves(pnode.board, tkn):
                cnode = Node(old_board=pnode.board,
                             move=move, oth=self.oth, token=B)
                next_node = self.minimax(depth+1, cnode, False, alpha, beta)

                best_node = self.max_node(best_node, next_node)
                alpha = self.max_node(alpha, best_node)

                if beta.score <= alpha.score:
                    break

            return best_node

        else:
            best_node = Node(score=INF)
            for move in self.oth.get_possible_moves(pnode.board, tkn):
                cnode = Node(old_board=pnode.board,
                             move=move, oth=self.oth, token=W)

                next_node = self.minimax(depth+1, cnode, True, alpha, beta)
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
    board = score = move = None

    def __init__(self, old_board=None, move=None, oth=None, token=None, score=None):
        if oth and token and move:
            self.board = oth.test_move(oth.clone_test_board(
                old_board), token, move[0], move[1])
            self.move = move
        elif old_board:
            self.board = oth.clone_test_board(old_board)

        if oth:
            b, w = oth.get_points_test_board(self.board)
            self.score = b - w

        if score:
            self.score = score
