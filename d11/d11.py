filename = 'd11eg.txt'
filename = 'd11.txt'
with open(filename) as f:
    txt = f.read().splitlines()

monkeys = []
for l in txt:
    parts = l.strip().split(':')
    if parts[0].startswith('Monkey'):
        monkey = int(parts[0].split()[1])
        monkeys.append(dict())
    elif parts[0].startswith('Starting'):
        monkeys[monkey]['items'] = [int(x) for x in parts[1].strip().split(', ')]
    elif parts[0].startswith('Operation'):
        monkeys[monkey]['operation'] = eval('lambda old: ' + parts[1].split('=')[1])
    elif parts[0].startswith('Test'):
        monkeys[monkey]['test'] = int(parts[1].split()[-1])
    elif parts[0].startswith('If true'):
        monkeys[monkey][True] = int(parts[1].split()[-1])
    elif parts[0].startswith('If false'):
        monkeys[monkey][False] = int(parts[1].split()[-1])
    
from pprint import pprint
pprint(monkeys)

def rounds(n, manage):
    states = [m['items'].copy() for m in monkeys]
    business = [0]*len(monkeys)
    for _ in range(n):
        for i, m in enumerate(monkeys):
            business[i] += len(states[i])
            while len(states[i]) > 0:
                item = states[i].pop(0)
                result = monkeys[i]['operation'](item)
                result = manage(result)
                if result % monkeys[i]['test'] == 0:
                    states[monkeys[i][True]].append(result)
                else:
                    states[monkeys[i][False]].append(result)
    business.sort()
    return business[-1]*business[-2]

# part 1
print(rounds(20, lambda x: x//3))

# part 2
modulator = 1
for m in monkeys:
    modulator *= m['test']
print(rounds(10000, lambda x: x % modulator))
