filename = 'd20eg.txt'
filename = 'd20.txt'
with open(filename) as f:
    txt = f.read().splitlines()

n = len(txt)
input = [int(l) for l in txt]
position = list(range(n))

def part1():
    for i in range(n):
        p = position.index(i)
        t = input.pop(p)
        d = (p + t)
        input.insert(d % (n-1), t)
        t2 = position.pop(p)
        position.insert(d % (n-1), t2)

def getres():
    s = input.index(0)
    total = 0
    for j in range(3):
        total += input[(s+(j+1)*1000)%n]
    print(total)

part1()
getres()

# part 2
input = [int(l)*811589153 for l in txt]
position = list(range(n))
for _ in range(10):
    part1()
getres()
