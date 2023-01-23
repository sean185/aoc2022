import re
import math
from pprint import pprint

filename = 'd19eg.txt'
filename = 'd19.txt'
with open(filename) as f:
    txt = f.read().splitlines()

# blueprints = dict()
blueprints = list()
for line in txt:
    pattern = 'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'
    res = re.match(pattern, line).groups()
    # blueprints[res[0]] = {
        # 'ore': (int(res[1]), 0, 0), # (ore, clay, obsidian)
        # 'clay': (int(res[2]), 0, 0),
        # 'obsidian': (int(res[3]), int(res[4]), 0),
        # 'geode': (int(res[5]), 0, int(res[6]))
    # }
    # ('geode', 'obsidian', 'clay', 'ore')
    blueprints.append([
        (0, int(res[6]), 0, int(res[5])),
        (0, 0, int(res[4]), int(res[3])),
        (0, 0, 0, int(res[2])),
        (0, 0, 0, int(res[1])) 
    ])

pprint(blueprints)

'''
DECISION TREE: decide what to do next, and wait until done
start
|- build ore bot
|- build clay bot
|- build obsidian bot
\- build geode bot
'''

def step_mats(state, n):
    state[8] += n
    for i in range(4):
        state[i+4] += state[i]*n

def step_make(state, plan):
    for i in range(4):
        state[i+4] -= plan[i]


# simple recursion
# state is (a, b, c, d, w, x, y, z, t)
#          (  robot  ) ( material ) time
def part1(blueprint, state, depth=0):
    global best
    global visited
    if state in visited:
        return visited[state]
    if state[8] >= max_time:
        if state[4] > best[4]:
            best = state[:]
        return state
    if state[4]+sum(range(state[0],state[0]+max_time-state[8])) < best[4]:
        # prune early if there's not enough time anyway
        return None
    newstates = []
    # branch decision tree of what to BUILD here
    for i in range(4): # ('geode', 'obsidian', 'clay', 'ore') # robots
        plan = blueprint[i]
        if any([state[j] == 0 for j in range(4) if plan[j] > 0]):
            # not possible as there are no robots to begin with
            # print('skipping', state, plan, depth)
            continue
        # print('planning for', ('geode', 'obsidian', 'clay', 'ore')[i], 'robot', state)
        # print([-((state[j+4] - plan[j]) // state[j]) for j in range(4) if plan[j] > 0])
        wait = max([-((state[j+4] - plan[j]) // state[j]) for j in range(4) if plan[j] > 0])
        newstate = list(state)
        if wait + 1 > max_time - state[8]:
            # exit early if this plan does not work out
            step_mats(newstate, max_time - state[8])
            newstates.append(tuple(newstate))
            continue
        if wait > 0:
            step_mats(newstate, wait)
        step_mats(newstate, 1)
        step_make(newstate, plan)
        newstate[i] += 1
        # print(newstate)
        newstates.append(tuple(newstate))
    result = [part1(blueprint, s, depth + 1) for s in newstates]
    result = [s for s in result if s is not None]
    # return result
    if len(result) == 0:
        return state
    else:
        # print(result)
        joined = max(result, key = lambda x : x[4])
        visited[state] = joined
        return joined

# part 1
max_time = 24
total = 0
for i, blueprint in enumerate(blueprints):
    # optimality: how fast does an tree reach geode? x @ y
    visited = dict()
    best = (0, 0, 0, 1, 0, 0, 0, 0, 0)
    r = part1(blueprint, best)
    print(r)
    total += (i+1)*r[4]
print(total)

# part 2
max_time = 32
total = 1
for i, blueprint in enumerate(blueprints[:3]):
    # optimality: how fast does an tree reach geode? x @ y
    visited = dict()
    best = (0, 0, 0, 1, 0, 0, 0, 0, 0)
    r = part1(blueprint, best)
    print(r)
    total *= r[4]
print(total)
