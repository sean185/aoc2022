filename = 'd18eg.txt'
filename = 'd18.txt'
with open(filename) as f:
    txt = f.read().splitlines()

points = {tuple(int(i) for i in l.split(',')) for l in txt}
dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

def add(point, delta):
    return tuple(x+d for x, d in zip(point, delta))

def part1(points):
    # total number of faces - faces that have neighbours
    total = len(points) * 6
    for point in points:
        for d in dirs:
            if add(point, d) in points:
                total -= 1
    return total

print(part1(points))

def part2(points):
    # create a cube superset, and flood-fill the outer volume
    bounds = [(min(ax), max(ax)) for ax in zip(*points)]
    print(bounds)

    cube = set()
    xbounds, ybounds, zbounds = bounds
    for x in range(xbounds[0]-1, xbounds[1]+1):
        for y in range(ybounds[0]-1, ybounds[1]+1):
            for z in range(zbounds[0]-1, zbounds[1]+1):
                cube.add((x, y, z))

    visited = set()
    search = {tuple(b[0] for b in bounds)}
    while len(search) > 0:
        point = search.pop()
        visited.add(point)
        for d in dirs:
            newpoint = add(point, d)
            if newpoint in points:
                continue
            elif newpoint in visited:
                continue
            elif newpoint in search:
                continue
            elif newpoint in cube:
            # elif all([bnd[0] <= p <= bnd[1] for p, bnd in zip(newpoint, bounds)]):
                search.add(newpoint)
    
    volume = cube.difference(visited)
    return part1(volume)

print(part2(points))
