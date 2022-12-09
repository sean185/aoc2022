def parse(filename):
    with open(filename) as f:
        txt = f.read()
    picture, instructions = [x.splitlines() for x in txt.split('\n\n')]
    positions = [i for i, x in enumerate(picture[-1]) if x != ' ']
    crates = [[row[p] for row in picture[-2::-1] if row[p] != ' '] for p in positions]
    steps = []
    for ins in instructions:
        _, num, _, st, _, ed = ins.split(' ')
        steps.append([int(x) for x in (num, st, ed)])
    return crates, steps

def part1(crates, steps):
    for step in steps:
        num, st, ed = step
        grabbed = []
        for i in range(num):
            grabbed.append(crates[st-1].pop())
        crates[ed-1].extend(grabbed)
    return ''.join([c.pop() for c in crates])

def part2(crates, steps):
    for step in steps:
        num, st, ed = step
        grabbed = []
        for i in range(num):
            grabbed.append(crates[st-1].pop())
        grabbed.reverse()
        crates[ed-1].extend(grabbed)
    return ''.join([c.pop() for c in crates])

filename = 'd05eg.txt'
filename = 'd05.txt'
output = part1(*parse(filename))
print(output)
output = part2(*parse(filename))
print(output)
