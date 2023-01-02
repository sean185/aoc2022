import re
from pprint import pprint

filename = 'd15eg.txt'; ypos = 10
filename = 'd15.txt'; ypos = 2000000

with open(filename) as f:
    txt = f.read().splitlines()

def mdist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def parse_input(txt):
    p = re.compile('(-?\d+)')
    sensors = []
    beacons = []
    radii = []
    for t in txt:
        res = [int(x) for x in p.findall(t)]
        sensor = tuple(res[:2])
        sensors.append(sensor)
        beacon = tuple(res[2:])
        beacons.append(beacon)
        radii.append(mdist(sensor, beacon))
    return sensors, beacons, radii

sensors, beacons, radii = parse_input(txt)

# for each point along the line, check if it is in the proximity of any sensor
def part1(sensors, beacons, radii):
    xmin = min([s[0]-r for s, r in zip(sensors, radii)])
    xmax = max([s[0]+r for s, r in zip(sensors, radii)])
    ymin = min([s[1]-r for s, r in zip(sensors, radii)])
    ymax = max([s[1]+r for s, r in zip(sensors, radii)])
    withinrange = 0
    for i in range(xmin, xmax+1):
        point = (i, ypos)
        if point in beacons:
            continue
        if point in sensors:
            continue
        for sensor, radius in zip(sensors, radii):
            if mdist(sensor, point) <= radius:
                withinrange += 1
                break
    print(withinrange)

part1(sensors, beacons, radii)

# part 2
ymax = ypos * 2
xmax = ypos * 2

def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)

def diagpoints(p1, p2):
    mag = abs(p1[0] - p2[0])
    d = [sign(c2 - c1) for c1, c2 in zip(p1, p2)]
    for i in range(mag):
        yield (p1[0]+d[0]*i, p1[1]+d[1]*i)

# create manhattan circle for each sensor
# iterate only along circumference
# check overlaps with other circles 
def part2(sensors, beacons, radii):
    overlaps = dict()
    for sensor, radius in zip(sensors, radii):
        outer = radius + 1
        top = (sensor[0], sensor[1] + outer)
        down = (sensor[0], sensor[1] - outer)
        left = (sensor[0] - outer, sensor[1])
        right = (sensor[0] + outer, sensor[1])
        for start, end in ((top, right), (right, down), (down, left), (left, top)):
            for point in diagpoints(start, end):
                if not (0 <= point[0] <= xmax) and (0 <= point[1] <= ymax):
                    continue
                for sensor2, radius2 in zip(sensors, radii):
                    if sensor == sensor2:
                        continue
                    outer2 = radius2 + 1
                    if mdist(sensor2, point) == outer2:
                        overlaps[point] = overlaps.get(point, 0) + 1

    most = max(overlaps.values())
    missing = [item[0] for item in overlaps.items() if item[1] == most][0]
    print(missing[0]*4000000+missing[1])

part2(sensors, beacons, radii)
