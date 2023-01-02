import re
from pprint import pprint

filename = 'd16eg.txt'
filename = 'd16.txt'
with open(filename) as f:
    lines = f.read().splitlines()

flowrates = dict()
edges = dict()
pat = re.compile('([A-Z]{2}|\d+)')
for line in lines:
    valve, flow, *links = pat.findall(line)
    flowrates[valve] = int(flow)
    edges[valve] = links
pprint(edges)

def part1():
    # state keeps track of (current position, open valves, total pressure)
    states = [('AA', set(), False, 0)]
    for _ in range(30):
        newstates = list()
        while len(states):
            node, openvalves, justarrived, pressure = states.pop(0)
            # print(node, openvalves, justarrived, pressure)
            accumulated = sum([flowrates[v] for v in openvalves])
            if justarrived and flowrates[node] > 0 and node not in openvalves:
                newstates.append((node, openvalves.union({node}), False, pressure+accumulated))
            for link in edges[node]:
                newstates.append((link, openvalves, True, pressure+accumulated))
        newstates = sorted(newstates, reverse=True, key=lambda x: x[3])
        if len(newstates) > 10000:
            newstates = newstates[:10000]
        states = newstates
    print(newstates[0])

part1()

def part2():
    # state keeps track of (current position, open valves, total pressure)
    states = [('AA', 'AA', set(), False, False, 0)]
    for _ in range(26):
        newstates = list()
        while len(states):
            me, el, openvalves, me_arr, el_arr, pressure = states.pop(0)
            # print(me, elephant, openvalves, justarrived, pressure)
            accumulated = sum([flowrates[v] for v in openvalves])
            me_options = []
            if me_arr and flowrates[me] > 0 and me not in openvalves:
                me_options.append((me, openvalves.union({me}), False))
            for link in edges[me]:
                me_options.append((link, openvalves, True))
            el_options = []
            if el_arr and flowrates[el] > 0 and el not in openvalves:
                el_options.append((el, openvalves.union({el}), False))
            for link in edges[el]:
                el_options.append((link, openvalves, True))
            # permutate all ways
            for me_node, me_valves, me_state in me_options:
                for el_node, el_valves, el_state in el_options:
                    newstates.append((me_node, el_node, me_valves.union(el_valves), me_state, el_state, pressure+accumulated))
        newstates = sorted(newstates, reverse=True, key=lambda x: x[5])
        if len(newstates) > 10000:
            newstates = newstates[:10000]
        states = newstates
    print(newstates[0])

part2()
