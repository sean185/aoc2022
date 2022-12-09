def dirsizes(filename):
    with open(filename) as f:
        txt = f.read().splitlines()
    dirs = {('/',):0}
    path = []
    for l in txt:
        p = l.split(' ')
        if l == '$ cd ..':
            cur = path.pop()
            dirs[tuple(path)] += dirs[tuple(path)+(cur,)]
        elif l.startswith('$ cd '):
            path.append(p[2])
        elif p[0] == '$':
            continue 
        elif p[0] == 'dir':
            dirs[tuple(path)+(p[1],)] = 0
        else:
            dirs[tuple(path)] += int(p[0])
    # wrap up summation of dir sizes as we roll up to root 
    while len(path) > 1:
        cur = path.pop()
        dirs[tuple(path)] += dirs[tuple(path)+(cur,)]
    return dirs

filename = 'd07eg.txt'
filename = 'd07.txt'

def part1(dirs):
    return sum([x for x in dirs.values() if x <= 100000])

output = part1(dirsizes(filename))
print(output)

def part2(dirs):
    free = 70000000 - dirs[('/',)]
    need = 30000000 - free
    return min([x for x in dirs.values() if x >= need])

output = part2(dirsizes(filename))
print(output)
