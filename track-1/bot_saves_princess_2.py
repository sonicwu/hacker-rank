#!/bin/python
# Head ends here
def nextMove(n, x, y, grid):
    # the input x and y are reversed
    startX, startY = y, x
    
    '''find the princess node.'''
    endX, endY = 0, 0
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == "p":
                endX = j
                endY = i

    '''path finding'''
    deltaX = endX - startX
    if deltaX > 0:
        print "RIGHT";
        return
    elif deltaX < 0:
        print "LEFT"
        return

    deltaY = endY - startY
    if deltaY > 0:
        print "DOWN"
        return
    elif deltaY < 0:
        print "UP"
        return

# Tail starts here
n = input()
x,y = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

nextMove(n, x, y, grid)