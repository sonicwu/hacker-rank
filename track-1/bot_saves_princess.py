#!/bin/python
# Head ends here
def nextMove(m, grid):
    '''find start node and end node.'''
    startX, startY = 0, 0
    endX, endY = 0, 0
    
    for i in range(m):
        for j in range(len(grid[i])):
            if grid[i][j] == "m":
                startX = j
                startY = i
            elif grid[i][j] == "p":
                endX = j
                endY = i
    
    '''path finding'''
    output = ''

    deltaX = endX - startX
    if deltaX > 0:
        output += "RIGHT\n" * abs(deltaX)
    else:
        output += "LEFT\n" * abs(deltaX)

    deltaY = endY - startY
    if deltaY > 0:
        output += "DOWN\n" * abs(deltaY)
    else:
        output += "UP\n" * abs(deltaY)

    return output

# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

print nextMove(m, grid)