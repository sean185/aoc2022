# AOC day 2
RPS = {'X': 1, 'Y': 2, 'Z':3}
part1_score_map = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    }
}

def part1(inputfile):
    with open(inputfile) as f:
        txt = f.read().splitlines()
    tally = 0
    for l in txt:
        them, me = l.split(" ")
        tally += RPS[me] + part1_score_map[them][me]
    return tally

print(part1('d02eg.txt'))
print(part1('d02.txt'))


part2_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def part2(inputfile):
    with open(inputfile) as f:
        txt = f.read().splitlines()
    tally = 0
    for l in txt:
        them, me = l.split(" ")
        for k, v in part1_score_map[them].items():
            if v == part2_map[me]:
                tally += RPS[k] + v
                break
    return tally

print(part2('d02eg.txt'))
print(part2('d02.txt'))
