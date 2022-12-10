filename = 'd09eg.txt'
filename = 'd09.txt'
with open(filename) as f:
    instructions = f.read().splitlines()

UDLR = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

sign = lambda x: bool(x > 0) - bool(x < 0)

def move(dir):
    displacement = UDLR[dir]
    knots[0] = (knots[0][0] + displacement[0], knots[0][1] + displacement[1])
    for i in range(1, len(knots)):
        displacement = (knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1])
        if max([abs(displacement[0]), abs(displacement[1])]) > 1:
            knots[i] = (knots[i][0] + sign(displacement[0]), knots[i][1] + sign(displacement[1]))
    states.append(knots[-1])

# part 1
knots = [(0, 0)]*2
states = []

for ins in instructions:
    dir, mag = ins.split(' ')
    mag = int(mag)
    for _ in range(mag):
        move(dir)
    
print(len(set(states)))


# part 2
knots = [(0, 0)]*10
states = []

for ins in instructions:
    dir, mag = ins.split(' ')
    mag = int(mag)
    for _ in range(mag):
        move(dir)
    
print(len(set(states)))

