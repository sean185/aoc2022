# AOC day 1
def part1(inputfile):
    with open(inputfile) as f:
        txt = f.read().splitlines()
    calories = []
    curr = 0
    for i in txt:
        if i == '':
            calories.append(curr)
            curr = 0
        else:
            curr += int(i)
    calories.append(curr)
    return calories

print(max(part1('d01eg.txt')))
print(max(part1('d01.txt')))

def part2(inputfile):
    calories = part1(inputfile)
    calories.sort(reverse=True)
    return calories[:3]
    
print(sum(part2('d01eg.txt')))
print(sum(part2('d01.txt')))
