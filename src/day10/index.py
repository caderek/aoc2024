import re
from itertools import product

with open('input.txt') as file:
    input = file.read().strip().splitlines()

TRAIL_LEN = 10
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
indicies = set(range(len(input)))
graph = {}
starts = []

for y, x,  in product(indicies, repeat=2):
    if input[y][x] == '.':
        continue
    val = int(input[y][x])
    key = (val, y, x)
    graph[key] = []
    if val == 0:
        starts.append(key)
    for dx, dy in dirs:
        yy = y + dy
        xx = x + dx
        if yy in indicies and xx in indicies:
            if input[yy][xx] == '.':
                continue
            val2 = int(input[yy][xx])
            if val2 - val == 1:
                graph[key].append((val2, yy, xx))

def get_ends(graph, start, count = 1):
    ends = []
    if count == TRAIL_LEN:
        ends.append(start)
    for neighbor in graph[start]:
        ends.extend(get_ends(graph, neighbor, count + 1))
    return ends


part1 = 0
part2 = 0

for start in starts:
    ends = get_ends(graph, start)
    part1 += len(set(ends))
    part2 += len(ends)

print(part1)
print(part2)
