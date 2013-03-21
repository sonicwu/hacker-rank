#!/bin/python
# Head ends here
def nextMove(m, grid):
    # find start node and end node.
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    
    # the input x and y were reversed in Hackerrank puzzles.
    for i in range(m):
        for j in range(len(grid[i])):
            if grid[i][j] == "m":
                start_x = j
                start_y = i
            elif grid[i][j] == "p":
                end_x = j
                end_y = i
    
    # path finding.
    output = ''

    delta_x = end_x - start_x
    if delta_x > 0:
        output += "RIGHT\n" * abs(delta_x)
    elif delta_x < 0:
        output += "LEFT\n" * abs(delta_x)

    delta_y = end_y - start_y
    if delta_y > 0:
        output += "DOWN\n" * abs(delta_y)
    elif delta_y < 0:
        output += "UP\n" * abs(delta_y)

    return output

# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

print nextMove(m, grid)