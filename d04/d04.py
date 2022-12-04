def getlines(inputfile):
    with open(inputfile) as f:
        txt = f.read().splitlines()
    return txt

def getrange(t):
    # "2-4"
    s, e = [int(x) for x in t.split('-')]
    return "".join([chr(48+x) for x in range(s, e + 1)])

def part1(txt):
    tally = 0
    for l in txt:
        r1, r2 = [getrange(x) for x in l.split(',')]
        tally += (r1 in r2) or (r2 in r1)
    return tally

print(part1(getlines('d04eg.txt')))
print(part1(getlines('d04.txt')))

def part2(txt):
    tally = 0
    for l in txt:
        r1, r2 = [getrange(x) for x in l.split(',')]
        tally += 0<len(set(r1).intersection(set(r2)))
    return tally

print(part2(getlines('d04eg.txt')))
print(part2(getlines('d04.txt')))
