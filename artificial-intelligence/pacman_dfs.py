#!/usr/bin/python

# Head ends here
def nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid):
    explored_vertexes = []
    dfs(pacman_x, pacman_y, grid, explored_vertexes)
    print len(explored_vertexes)
    for v in explored_vertexes:
        print v[0], v[1]
    print len(explored_vertexes) - 1
    for v in explored_vertexes:
        print v[0], v[1]

    return

def get_adjacent_vertexes(vertex_x, vertex_y, grid):
    vertexex = []
    # DOWN -> RIGHT -> LEFT -> UP
    if vertex_x + 1 < len(grid) and grid[vertex_x + 1][vertex_y] in '-.':
        vertexex.append([vertex_x + 1, vertex_y])
    if vertex_y + 1 < len(grid[0]) and grid[vertex_x][vertex_y + 1] in '-.':
        vertexex.append([vertex_x, vertex_y + 1])
    if vertex_y > 0 and grid[vertex_x][vertex_y - 1] in '-.':
        vertexex.append([vertex_x, vertex_y - 1])
    if vertex_x > 0 and grid[vertex_x - 1][vertex_y] in '-.':
        vertexex.append([vertex_x - 1, vertex_y])

    return vertexex

def dfs(vertex_x, vertex_y, grid, explored_vertexes):
    explored_vertexes.append([vertex_x, vertex_y])

    grid[vertex_x] = grid[vertex_x][0:vertex_y] + 'E' + grid[vertex_x][vertex_y + 1:]
    adjacent_vertexes = get_adjacent_vertexes(vertex_x, vertex_y, grid)
    for v in adjacent_vertexes:
        x = v[0]
        y = v[1]

        if grid[x][y] == '.':
            explored_vertexes.append([x, y])
            return True
        else:
            if dfs(x, y, grid, explored_vertexes):
                return True

# Tail starts here
pacman_x, pacman_y = [ int(i) for i in raw_input().strip().split() ]
food_x, food_y = [ int(i) for i in raw_input().strip().split() ]
x,y = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, x):
    grid.append(raw_input().strip())

'''
pacman_x = 3
pacman_y = 9
food_x = 5
food_y = 1
x = 7
y = 20

grid = []
grid.append("%%%%%%%%%%%%%%%%%%%%")
grid.append("%--------------%---%")
grid.append("%-%%-%%-%%-%%-%%-%-%")
grid.append("%--------P-------%-%")
grid.append("%%%%%%%%%%%%%%%%%%-%")
grid.append("%.-----------------%")
grid.append("%%%%%%%%%%%%%%%%%%%%")
'''

nextMove(x, y, pacman_x, pacman_y, food_x, food_y, grid)