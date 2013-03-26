#!/bin/python
import random

class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

def next_move(posx, posy, board):
    # the input x and y were reversed in Hackerrank puzzles.
    bot_node = Node(posy, posx)

    dirty_nodes = []
    fogged_nodes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            node = Node(j, i)
            if board[i][j] == "d":
                dirty_nodes.append(node)
            elif board[i][j] == "o":
                fogged_nodes.append(node)

    # find the nearest dirty node.
    nearest_dirty_node = None
    for node in dirty_nodes:
        if nearest_dirty_node is None or node.distTo(bot_node) < nearest_dirty_node.distTo(bot_node):
            nearest_dirty_node = node

    if nearest_dirty_node is None:
        move_to_fog(bot_node, fogged_nodes)
    else:
        move_to_node(nearest_dirty_node.x - bot_node.x, nearest_dirty_node.y - bot_node.y)
        return

def move_to_fog(bot_node, fogged_nodes):
    if len(fogged_nodes) == 0:
        return

    # find the best move to clear fogs.
    search_scope = 2
    move_direction = None
    while move_direction is None:
        #[left, right, up, down]
        weights = [0, 0, 0, 0]

        for node in fogged_nodes:
            delta_x = node.x - bot_node.x
            delta_y = node.y - bot_node.y

            if abs(delta_y) < search_scope:
                if delta_x == search_scope:
                    weights[1] += 1 # right
                elif delta_x == -search_scope:
                    weights[0] += 1 # left
            
            if abs(delta_x) < search_scope:
                if delta_y == search_scope:
                    weights[3] += 1 # down
                elif delta_y == -search_scope:
                    weights[2] += 1 # up

        idx = weights.index(max(weights))
        temp_directions = []
        for i in range(len(weights)):
            if weights[i] == weights[idx]:
                if i == 0:
                    temp_directions.append("LEFT")
                elif i == 1:
                    temp_directions.append("RIGHT")
                elif i == 2:
                    temp_directions.append("UP")
                elif i == 3:
                    temp_directions.append("DOWN")

        move_direction = random.choice(temp_directions)

    print move_direction

def move_to_node(delta_x, delta_y):
    if delta_x < 0 :
        print "LEFT"
    elif delta_x > 0 :
        print "RIGHT"
    elif delta_y < 0 :
        print "UP"
    elif delta_y > 0 :
        print "DOWN"
    else:
        print "CLEAN"

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)