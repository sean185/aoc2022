
filename = 'd23eg2.txt'
filename = 'd23eg.txt'
filename = 'd23.txt'

with open(filename) as f:
    txt = f.read().splitlines()

elves = list()
for y, row in enumerate(txt):
    for x, c in enumerate(row):
        if c == '#':
            elves.append((x,y))

print(elves)
directions = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
order = list('NSWE')

def get_bounds(points):
    xmin, xmax, ymin, ymax = float('inf'), float('-inf'), float('inf'), float('-inf')
    for x, y in points:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return xmin, xmax, ymin, ymax

print(get_bounds(elves))

def get_adj(point):
    x, y = point
    nbs = [(x+dx, y+dy) for dx, dy in directions]
    return nbs

def has_nbs(point):
    overlap = set(get_adj(point)).intersection(set(elves))
    return len(overlap) > 0

checks = {
    'N': ((-1, -1), (0, -1), (1, -1)),
    'S': ((-1, 1), (0, 1), (1, 1)),
    'W': ((-1, -1), (-1, 0), (-1, 1)),
    'E': ((1, -1), (1, 0), (1, 1))
}

def get_next(point):
    x, y = point
    for d in order:
        look = [(x+dx, y+dy) for dx, dy in checks[d]]
        if len(set(look).intersection(set(elves))) == 0:
            return look[1]
    return point

def step():
    # determine which elves will move at all
    should_move = [has_nbs(elf) for elf in elves]
    # determine proposed step of elves
    proposed = []
    counts = dict()
    for i in range(len(elves)):
        elf = elves[i]
        if should_move[i]:
            next_point = get_next(elf)
        else:
            next_point = elf
        proposed.append(next_point)
        counts[next_point] = counts.get(next_point, 0) + 1
    # determine if any movement will take place
    for i in range(len(elves)):
        elf = elves[i]
        p = proposed[i]
        # print(elves[i], p, counts[p], should_move[i])
        if not should_move[i]:
            continue
        if counts[p] > 1:
            continue
        elves[i] = p
    # make movements, and move order
    order.append(order.pop(0))

def render():
    xmin, xmax, ymin, ymax = get_bounds(elves)
    output = ''
    for j in range(ymin, ymax+1):
        for i in range(xmin, xmax+1):
            output += '#' if (i, j) in elves else '.'
        output += '\n'
    print(output)

def part1(n):
    render()
    for i in range(n):
        print(i+1, order)
        step()
        render()
    xmin, xmax, ymin, ymax = get_bounds(elves)
    print((xmax-xmin+1)*(ymax-ymin+1)-len(elves))

part1(10)

# keep a note of prev vs curr, exiting when steady state found
def part2(n):
    last = list(elves)
    # render()
    for i in range(n):
        print(i+1)
        step()
        # render()
        if last == elves:
            print('done!', i+1)
            break
        else:
            last = list(elves)
    render()
    xmin, xmax, ymin, ymax = get_bounds(elves)
    print((xmax-xmin+1)*(ymax-ymin+1)-len(elves))

part2(100000)
