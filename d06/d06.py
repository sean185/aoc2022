filename = 'd06eg.txt'
filename = 'd06.txt'
with open(filename) as f:
    lines = f.read().splitlines()

def func(num, input):
    buffer = ''
    for i, c in enumerate(input):
        if len(buffer) == num:
            buffer = buffer[1:]
        buffer += c
        if len(set(buffer))==num:
            return i+1

# part 1
for l in lines:
    print(func(4, l))

# part 2
for l in lines:
    print(func(14, l))
