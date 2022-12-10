from pprint import pprint 

def get_trees(filename):
    with open(filename) as f:
        txt = f.read().splitlines()
    return [[int(x) for x in l] for l in txt]

def count_trees(trees, visible, seq):
    for row in seq:
        curr_max = -1
        for i, j in row:
            t = trees[i][j]
            if t > curr_max:
                curr_max = t
                visible[i][j] = True

def part1():
    trees = get_trees(filename)
    size = len(trees) # assume square
    visible = [[False for y in range(size)] for x in range(size)]

    fromleft = [[(x, y) for y in range(size)] for x in range(size)]
    fromright = [[(x, y) for y in reversed(range(size))] for x in range(size)]
    fromup = [[(y, x) for y in range(size)] for x in range(size)]
    fromdown = [[(y, x) for y in reversed(range(size))] for x in range(size)]

    count_trees(trees, visible, fromleft)
    count_trees(trees, visible, fromright)
    count_trees(trees, visible, fromup)
    count_trees(trees, visible, fromdown)
    
    print(sum([sum(r) for r in visible]))

def count_4ways(trees, score, x, y):
    size = len(trees)
    def count_max_trees(seq):
        counter = 0
        for i, j in seq:
            counter += 1
            if trees[i][j] >= trees[x][y]:
                break
        return counter
    score[x][y] *= count_max_trees([(i, y) for i in range(x-1, -1, -1)])
    score[x][y] *= count_max_trees([(i, y) for i in range(x+1, size)])
    score[x][y] *= count_max_trees([(x, j) for j in range(y-1, -1, -1)])
    score[x][y] *= count_max_trees([(x, j) for j in range(y+1, size)])

def part2():
    trees = get_trees(filename)
    size = len(trees) # assume square
    score = [[1 for y in range(size)] for x in range(size)]

    for x in range(size):
        for y in range(size):
            count_4ways(trees, score, x, y)

    print(max([max(r) for r in score]))

filename = 'd08.txt'
part1()
part2()