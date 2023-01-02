import re
import os
from pprint import pprint 
from time import sleep

filename = 'd22eg.txt'
filename = 'd22.txt'
with open(filename) as f:
    txt = f.read().splitlines()

directions = txt[-1]
instructions = re.findall(r'(\d+|\w)', directions)

map = [list(r) for r in txt[:-2]]
curr = (txt[:-2][0].index('.'), 0)
facing = 0 # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

opentiles = set()
solidwalls = set()
for y, row in enumerate(txt[:-2]):
    for x, pixel in enumerate(row):
        if pixel == '.':
            opentiles.add((x, y))
        elif pixel == '#':
            solidwalls.add((x, y))

allpoints = opentiles.union(solidwalls)
xmax = max(p[0] for p in allpoints) + 1
ymax = max(p[1] for p in allpoints) + 1

def getnext(curr, dir):
    # blanks, handle wrapping, broken lines
    i = 1
    reached = False
    while not reached:
        next = ((curr[0]+i*dir[0])%xmax, (curr[1]+i*dir[1])%ymax)
        if next in solidwalls:
            reached = True
            return curr
        elif next in opentiles:
            reached = True
            map[next[1]][next[0]] = '>v<^'[facing % 4]
            return next
        i += 1

def render():
    os.system('cls')
    output = '\n'.join([''.join(r) for r in map])
    print(output)

facemapping = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)} # (x, y) > v < ^
for inst in instructions:
    if inst.isnumeric():
        n = int(inst) # loop counter 
        dir = facemapping[facing % 4]
        for _ in range(n):
            curr = getnext(curr, dir)
    else:
        if inst == 'R':
            facing += 1
        else:
            facing += -1
    map[curr[1]][curr[0]] = '>v<^'[facing % 4]
    # print(curr, facing, inst)
    # render()
    # sleep(2)

print(curr, facing)
result = [(curr[1]+1)*1000, (curr[0]+1)*4, facing%4]
print(sum(result))

edgemap = dict()
# for i in range(4):
    # edgemap[(8+i, 0)] = ((4-i, 4), 1) # 1
    # edgemap[(4-i, 4)] = ((8+i, 0), 1) # 1'
    # edgemap[(11, 0+i)] = ((15, 11-i), 2) # 2
    # edgemap[(15, 11-i)] = ((11, 0+i), 2) # 2'
    # edgemap[(11, 4+i)] = ((15-i, 8), 1) # 3
    # edgemap[(15-i, 8)] = ((11, 4+i), 2) # 3'
    # edgemap[(8, 0+i)] = ((4+i, 4), 1) # 4
    # edgemap[(4+i, 4)] = ((8, 0+i), 0) # 4'
    # edgemap[(0, 4+i)] = ((15-i, 11), 3) # 5
    # edgemap[(15-i, 11)] = ((0, 4+i), 0) # 5'
    # edgemap[(0+i, 7)] = ((11-i, 11), 3) # 6
    # edgemap[(11-i, 11)] = ((0+i, 7), 3) # 6'
    # edgemap[(4+i, 7)] = ((8, 11-i), 0) # 7
    # edgemap[(8, 11-i)] = ((4+i, 7), 3) # 7'
# pprint(edgemap)

for i in range(50):
    edgemap[(50+i, 0, 3)] = (0, 150+i, 0) # 1
    edgemap[(0, 150+i, 2)] = (50+i, 0, 1) # 1'
    edgemap[(100+i, 0, 3)] = (i, 199, 3) # 2
    edgemap[(i, 199, 1)] = (100+i, 0, 1) # 2'
    edgemap[(149, i, 0)] = (99, 149-i, 2) # 3
    edgemap[(99, 149-i, 0)] = (149, i, 2) # 3'
    edgemap[(100+i, 49, 1)] = (99, 50+i, 2) # 4
    edgemap[(99, 50+i, 0)] = (100+i, 49, 3) # 4'
    edgemap[(50+i, 149, 1)] = (49, 150+i, 2) # 5
    edgemap[(49, 150+i, 0)] = (50+i, 149, 3) # 5'
    edgemap[(0, 100+i, 2)] = (50, 49-i, 0) # 6
    edgemap[(50, 49-i, 2)] = (0, 100+i, 0) # 6'
    edgemap[(50, 50+i, 2)] = (i, 100, 1) # 7
    edgemap[(i, 100, 3)] = (50, 50+i, 0) # 7'


def getnext(curr, dir):
    global facing
    # blanks, handle wrapping, broken lines
    next = ((curr[0]+dir[0]), (curr[1]+dir[1]))
    if next in solidwalls:
        return curr, dir
    elif next in opentiles:
        map[next[1]][next[0]] = '>v<^'[facing % 4]
        return next, dir
    else:
        # off map!
        x, y, newfacing = edgemap[curr+(facing%4,)]
        next = (x, y)
        if next in solidwalls:
            return curr, dir
        facing = newfacing
        map[next[1]][next[0]] = '>v<^'[facing % 4]
        # print(next, facing)
        return next, facemapping[facing]

map = [list(r) for r in txt[:-2]]
curr = (txt[:-2][0].index('.'), 0)
facing = 0 # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

for inst in instructions:
    if inst.isnumeric():
        n = int(inst) # loop counter 
        dir = facemapping[facing % 4]
        for _ in range(n):
            curr, dir = getnext(curr, dir)
    else:
        if inst == 'R':
            facing += 1
        else:
            facing += -1
    map[curr[1]][curr[0]] = '>v<^'[facing % 4]
    # print(curr, facing, inst)
    # render()
    # sleep(0.2)

print(curr, facing)
result = [(curr[1]+1)*1000, (curr[0]+1)*4, facing%4]
print(sum(result))

# too high: 159197