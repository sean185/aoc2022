alnum = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
scores = dict(zip(alnum, range(1,26*2+1)))

def getlines(inputfile):
    with open(inputfile) as f:
        txt = f.read().splitlines()
    return txt

def part1(txt):
    tally = 0
    for l in txt:
        mid = len(l)//2
        overlap = set(l[:mid]).intersection(set(l[mid:]))
        tally += scores[list(overlap)[0]]
    return tally

print(part1(getlines('d03eg.txt')))
print(part1(getlines('d03.txt')))

def part2(txt):
    tally = 0
    overlap = set()
    for i, l in enumerate(txt):
        if (i%3 == 0):
            overlap = set(l)
        overlap.intersection_update(set(l))
        if (i%3 == 2) and (i > 0):
            tally += scores[list(overlap)[0]]
    return tally

print(part2(getlines('d03eg.txt')))
print(part2(getlines('d03.txt')))
