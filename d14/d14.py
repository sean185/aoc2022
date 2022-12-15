filename = 'd14eg.txt'
filename = 'd14.txt'
with open(filename) as f:
    txt = f.read().splitlines()

sign = lambda x:(x > 0) - (x < 0)

rocks = set()
for l in txt:
    points = [[int(i) for i in x.split(',')] for x in l.split(' -> ')]
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        if p1[0] == p2[0]:
            for j in range(p1[1], p2[1], sign(p2[1] - p1[1])):
                rocks.add((p1[0], j))
        else:
            for i in range(p1[0], p2[0], sign(p2[0] - p1[0])):
                rocks.add((i, p1[1]))
    rocks.add(tuple(points[-1]))

source = (500, 0)
directions = {(0, 1), (-1, 1), (1, 1)}
xmin = min([r[0] for r in rocks])
xmax = max([r[0] for r in rocks])
ymax = max([r[1] for r in rocks])

import os
def render(rocks, sands):
    total = set([source]).union(rocks).union(sands)
    xmin = min([t[0] for t in total])
    xmax = max([t[0] for t in total])
    ymin = min([t[1] for t in total])
    ymax = max([t[1] for t in total])
    output = []
    for j in range(ymax-ymin+1):
        line = []
        for i in range(xmax-xmin+1):
            point = (i+xmin, j+ymin)
            if point == (500, 0):
                line.append('+')
            elif point in rocks:
                line.append('#')
            elif point in sands:
                line.append('o')
            else:
                line.append('.')
        output.append(''.join(line))
    print('\n'.join(output))

def part1():
    sands = set()
    def drop():
        pos = list(source)
        while True:
            valid = None
            for d in directions:
                newpos = (pos[0] + d[0], pos[1] + d[1])
                if not newpos in rocks.union(sands):
                    valid = list(newpos)
                    break
            if not valid:
                return pos
            pos = valid
            if not xmin <= valid[0] <= xmax:
                return None
            if not valid[1] <= ymax:
                return None
            
        return pos
    # sands.add(tuple(pos))
    dest = drop()
    while dest:
        sands.add(tuple(dest))
        render(rocks, sands)
        dest = drop()
    print(len(sands))

# part1()

def part2():
    sands = set()
    def drop():
        blocked = rocks.union(sands)
        pos = list(source)
        while True:
            valid = None
            # check directly below
            # then check sides
            for d in directions:
                newpos = (pos[0] + d[0], pos[1] + d[1])
                if not newpos in blocked:
                    valid = list(newpos)
                    break
            if not valid:
                return tuple(pos)
            pos = valid
            if not valid[1] <= ymax:
                return tuple(pos)
        return tuple(pos)

    dest = drop()
    while not dest == source:
        sands.add(dest)
        # render(rocks, sands)
        dest = drop()
    print(len(sands))

part2()

