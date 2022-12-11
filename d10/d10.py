filename = 'd10eg.txt'
filename = 'd10.txt'
with open(filename) as f:
    txt = f.read().splitlines()

states = [1]
for l in txt:
    states.append(states[-1])
    if l.startswith('addx'):
        states.append(states[-1]+int(l.split(' ')[1]))

pos = [20+40*x for x in range(6)]

# part 1
strength = 0
for p in pos:
    strength += p*states[p-1]

print(strength)

# part 2
picture = ''
for i in range(240):
    if i > 0 and i % 40 == 0:
        picture += '\n'
    picture += '#' if (states[i]-1 <= (i % 40) <= states[i]+1) else ' '

print(picture)