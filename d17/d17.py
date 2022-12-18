'''
 0123456 0123456 0123456 0123456 0123456 
0.......|.......|.......|..#....|.......
1.......|...#...|....#..|..#....|.......
2.......|..###..|....#..|..#....|..##...
3..####.|...#...|..###..|..#....|..##...
'''
rocks = [
    ((2, 3), (3, 3), (4, 3), (5, 3)),
    ((3, 1), (2, 2), (3, 2), (4, 2), (3, 3)),
    ((4, 1), (4, 2), (4, 3), (3, 3), (2, 3)),
    ((2, 0), (2, 1), (2, 2), (2, 3)),
    ((2, 2), (2, 3), (3, 2), (3, 3))
    ]

## The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

def readwinds(filename):
    with open(filename) as f:
        txt = f.read().strip()
    return txt

winds = readwinds('d17.txt')
# print(winds)

def render(map, rock):
    for i, row in enumerate(map):
        line = ''
        for j, pos in enumerate(row):
            line += '@' if (j, i) in rock else pos
        print(line)

def step(map, rock, wind):
    xax = [r[0] for r in rock]
    yax = [r[1] for r in rock]
    # check left/right by jet
    #   if reached, nothing
    #   if not, move
    newpos = [r[:] for r in rock]
    if wind == '>' and max(xax) < 6 and all([map[y][x+1] == '.' for x, y in newpos]):
        newpos = [(x+1, y) for x, y in rock]
    elif wind == '<' and min(xax) > 0 and all([map[y][x-1] == '.' for x, y in newpos]):
        newpos = [(x-1, y) for x, y in rock]
    else:
        pass # nothing to do
    # check down
    #   if reached, return
    #   if not, move
    stopped = False
    # render(map, newpos)
    if all([map[y+1][x] == '.' for x, y in newpos]):
        newpos = [(x, y+1) for x, y in newpos]
    else:
        # print('stopped!')
        stopped = True
        for x, y in newpos:
            map[y][x] = '#'

    return newpos, stopped

def sim(n):
    map = [list('-------')]
    j = 0
    for i in range(n):
        # print(i)
        rock = rocks[i % len(rocks)]
        stopped = False
        for _ in range(7):
            map.insert(0, list('.......'))
        while not stopped:
            # print('stepping...')
            wind = winds[j % len(winds)]
            rock, stopped = step(map, rock, wind)
            j += 1
        while all([r == '.' for r in map[0]]):
            map.pop(0)
    # render(map, [])
    print(len(map)-1)

# part 1
sim(2022)
