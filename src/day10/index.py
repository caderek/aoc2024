from itertools import product

with open('input.txt') as file:
    input = file.read().strip().splitlines()

TRAIL_LEN = 10
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
indicies = set(range(len(input)))
graph = {}
starts = []

for y, x,  in product(indicies, repeat=2):
    val = int(input[y][x])
    node = (y, x)
    graph[node] = []
    if val == 0:
        starts.append(node)
    for dx, dy in dirs:
        y2, x2 = y + dy, x + dx
        if y2 in indicies and x2 in indicies:
            val2 = int(input[y2][x2])
            if val2 - val == 1:
                graph[node].append((y2, x2))

def get_ends(graph, node, count = 1):
    ends = []
    if count == TRAIL_LEN:
        ends.append(node)
    for neighbor in graph[node]:
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
