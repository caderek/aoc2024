import sys
from functools import cache
from collections import deque, defaultdict
from itertools import pairwise

sys.setrecursionlimit(100000)

with open('input.txt') as file:
    input = file.read().strip()

input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

rows = input.splitlines()

size = len(rows)
indicies = set(range(size))

graph = defaultdict(list)
start = None
end = None

for y in indicies:
    for x in indicies:
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            yy, xx = y + dy, x + dx
            if (xx in indicies) and (yy in indicies) and rows[yy][xx] != '#':
                node = complex(yy, xx)
                graph[complex(y, x)].append(node)
                if rows[yy][xx] == 'S':
                    start = node
                elif rows[yy][xx] == 'E':
                    end = node

def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_paths(graph, node, end, path)

            for p in new_paths:
                paths.append(p)
    return paths

paths = all_paths(graph, start, end)

min_score = float('inf')

for path in paths:
    dir = complex(0, 1)
    score = 0
    for a, b in pairwise(path):
        adir = complex(b.real - a.real, b.imag - a.imag)
        score += 1
        same_dir = complex(adir.real - dir.real, adir.imag - dir.imag) == 0j
        if not same_dir:
            score += 2000 if complex(adir.real + dir.real, adir.imag + dir.imag) == 0j  else 1000
        dir = adir
    min_score = min(min_score, score)

print(min_score)

