import os
import matplotlib.pyplot as plt


'''
    Create file maze with gates
'''


# Map 1
with open('maze_with_gate1.txt', 'w') as outfile:
    outfile.write('2\n')
    outfile.write('8 3 4 7\n')
    outfile.write('9 19 6 13\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxx\n')
    outfile.write('x  xxxx xxxx             \n')
    outfile.write('x x  xxxxxxx  xxxx      x\n')
    outfile.write('x    xxxxx      xxxx    x\n')
    outfile.write('x      -   xx xxxx      x\n')
    outfile.write('xxx xxxxx xxx xx   xx   x\n')
    outfile.write('x    xxxxxxx -          x\n')
    outfile.write('x         xx xxx xx  xxxx\n')
    outfile.write('x  -    xxxx xxxxxxx   xx\n')
    outfile.write('x xx               -    x\n')
    outfile.write('x  x   xxxx  xx         x\n')
    outfile.write('x    S xxxxxx  xxxxxxxxxx\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxx')


# Map 2
with open('maze_with_gate2.txt', 'w') as outfile:
    outfile.write('3\n')
    outfile.write('6 19 1 3\n')
    outfile.write('8 20 7 5\n')
    outfile.write('3 17 2 12\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
    outfile.write('x  -        xxxx  xxxxx  xxxxx\n')
    outfile.write('   x  xxx   - xxx  xxxxxxxxxxx\n')
    outfile.write('x    xxxxx xxxxxx-xx     xxxxx\n')
    outfile.write('x       xx  xxxxx   xxxx   xxx\n')
    outfile.write('xxxxxx  x   xxxxxxxxxxxxx xxxx\n')
    outfile.write('xxxxx   xxxxxxxx   - xxxxxxxxx\n')
    outfile.write('xxx  -xxxxxxxxxxx  xxxxxxxx  x\n')
    outfile.write('x               S   -xxxxxxxxx\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')


# Map 3(big size map)
with open('maze_with_gate3.txt', 'w') as outfile:
    outfile.write('4\n')
    outfile.write('2 19 5 19\n')
    outfile.write('3 4 7 1\n')
    outfile.write('3 9 6 11\n')
    outfile.write('7 23 11 33\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
    outfile.write('xS                   xxxxxxxxxx   xx\n')
    outfile.write('x  xxxxxx  xxxxxxxx-  xxxxxxxx     x\n')
    outfile.write('x   -    -     xxxxxx x xxxxxxxxxxxx\n')
    outfile.write('x      xxxxxx xxxxxx  xxxxxxxxxxxxxx\n')
    outfile.write('x   xx  xxxx   xxxx- xxxx xxxxxxxxxx\n')
    outfile.write('xx x   xxxx-x  xxxxx x xxxxxxxxxxx x\n')
    outfile.write('x-      xxxxx  xxxxx   -  xxxxxx   x\n')
    outfile.write('xxxxx      x    xxxxxxxxxxxxxxx x  x\n')
    outfile.write('x        xxxxx     xxxxxxxxxxxxxx  x\n')
    outfile.write('x    xxx    xxxx   xxxxxxx         x\n')
    outfile.write('x xx      xxxxxxx    xxxxxxx xxx -xx\n')
    outfile.write('x       xx  xxxxxx xxxxxxx    x   xx\n')
    outfile.write('xxxxx                        xxxxxxx\n')
    outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxx\n')


'''
    Read file maze to store maze and gates
'''


def readFile(filename):
    f = open(filename, 'r')
    n_gates = int(next(f)[:-1])
    gates = {}

    for i in range(n_gates):
        # x1,y1: entrance point
        # x2, y2: exit point
        x1, y1, x2, y2 = map(int, next(f)[:-1].split(' '))
        gates[(x1, y1)] = (x2, y2)

    text = f.read()
    maze = [list(i) for i in text.splitlines()]
    f.close()

    return gates, maze


'''
    Find start and exit point in the maze
'''


def findStartAndExitPosition(maze):
    row, col = len(maze), len(maze[0])
    start = (0, 0)
    end = ''

    for i in range(row):
        for j in range(col):
            if (maze[i][j] == 'S'):
                start = (i, j)

            elif (maze[i][j] == ' '):
                if (i == 0) or (i == len(maze) - 1) or (j == 0) or (j == len(maze[0]) - 1):
                    end = (i, j)

            else:
                pass

    return (start, end)


def visualize_maze(maze, gates, start, end, route=None):
    """
    Args:
      1. maze: The maze read from the input file,
      2. gates: Collections of gate to change cell of node,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(maze))
             for j in range(len(maze[0])) if maze[i][j] == 'x']

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0]-route[i-1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0]-route[i-1][0] < 0:
                direction.append('^')  # v
            elif route[i][1]-route[i-1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        # direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(figsize=(10, 6), dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([item[0][1] for item in gates.items()], [-item[0][0] for item in gates.items()],
                marker='8', s=100, color='green', label='Entrance')

    plt.scatter([item[1][1] for item in gates.items()], [-item[1][0] for item in gates.items()],
                marker='8', s=100, color='purple', label='Exit')

    plt.scatter(start[1], -start[0], marker='*',
                s=100, color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1], -route[i+1][0],
                        marker=direction[i], color='silver')

    plt.text(end[1], -end[0], 'EXIT', color='red',
             horizontalalignment='center', verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc='lower right')
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')
