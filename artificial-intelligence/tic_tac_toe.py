#!/bin/python
import random

class Line:
    def __init__(self, neighbor_a, neighbor_b):
        self.neighbor_a = neighbor_a
        self.neighbor_b = neighbor_b

    def calc_weight(self):
        enemy_num = 0
        friendly_num = 0
        if self.neighbor_a.is_enemy != None:
            if self.neighbor_a.is_enemy:
                enemy_num += 1
            else:
                friendly_num += 1
        if self.neighbor_b.is_enemy != None:
            if self.neighbor_b.is_enemy:
                enemy_num += 1
            else:
                friendly_num += 1

        # "_XX" or "OO_", will WIN or LOSE.
        if enemy_num == 2 or friendly_num == 2:
            return 10000

        if enemy_num == 0:
            # "__O", CHECKMATE!
            if friendly_num == 1:
                return 1000
            else: # "___", line is empty, ATTACK!
                return 5

        if friendly_num == 0:
            # "__X", DEFEND!
            if enemy_num == 1:
                return 2

        # "_OX", NULL.
        return 0

class Node:
    def __init__(self, x=0, y=0, is_enemy=None):
        self.x = x
        self.y = y
        self.is_enemy = is_enemy
        self.total_weight = 0

    def __str__(self):
        return "Node[{0}, {1}] Weight:{2}".format(self.x, self.y, self.total_weight)

# Complete the function below to print 2 integers separated by a single space which will be your next move 
def next_move(player, board):
    highest_weight_node = None

    # find all empty nodes.
    length = len(board)
    for x in range(length):
        for y in range(len(board[x])):
            # NOTE: In Hackerrank puzzles, the top left is (0, 0), the horizontal coordinate is 'y', the vertical coordinate is 'x'.
            if board[x][y] == "_":
                weight = 0

                # build horizontal line.
                horizontal_line = Line(
                    build_neighbor_node((x + 1) % length, y, board, player),
                    build_neighbor_node((x + 2) % length, y, board, player))
                weight += horizontal_line.calc_weight()
                
                # build vertical line.
                vertical_line = Line(
                    build_neighbor_node(x, (y + 1) % length, board, player),
                    build_neighbor_node(x, (y + 2) % length, board, player))
                weight += vertical_line.calc_weight()
                
                # build the "forward slash" line.
                if x == y:
                    forward_slash_line = Line(
                        build_neighbor_node((x + 1) % length, (y + 1) % length, board, player),
                        build_neighbor_node((x + 2) % length, (y + 2) % length, board, player))
                    weight += forward_slash_line.calc_weight()
                    
                # build the "backslash" line.
                if y + x == 2:
                    backslash_line = Line(
                        build_neighbor_node((x + 1) % length, 2 - (x + 1) % length, board, player),
                        build_neighbor_node((x - 1) % length, 2 - (x - 1) % length, board, player))
                    weight += backslash_line.calc_weight()
                    
                if highest_weight_node == None or weight > highest_weight_node.total_weight:
                    highest_weight_node = Node(x, y)
                    highest_weight_node.total_weight = weight

    print highest_weight_node.x, highest_weight_node.y

def build_neighbor_node(x, y, board, player):
    if board[x][y] == "_":
        return Node(x, y)
    else:
        return Node(x, y, board[x][y] != player)

# If player is X, I'm the first player.
# If player is O, I'm the second player.
player = raw_input()

# Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append(raw_input())

next_move(player, board)