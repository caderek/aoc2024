import math
import re
from itertools import combinations

with open('input.txt') as file:
    input = [[*line] for line in file.read().strip().splitlines()]

size = len(input)
indicies = range(size)
antennas = {}

for y in indicies:
    for x, val in enumerate(input[y]):
        if val != '.':
            antennas.setdefault(val, []).append((y, x))

def solve1():
    antinodes = set()

    for coords in antennas.values():
        for a, b in combinations(coords, 2):
            distY = a[0] - b[0]
            distX = a[1] - b[1]

            aa = (a[0] + distY, a[1] + distX)
            bb = (b[0] - distY, b[1] - distX)

            aa_in = aa[0] in indicies and aa[1] in indicies
            bb_in = bb[0] in indicies and bb[1] in indicies

            if aa_in:
                antinodes.add(aa)
            if bb_in:
                antinodes.add(bb)

    return len(antinodes)

def solve2():
    antinodes = set()

    for coords in antennas.values():
        for a, b in combinations(coords, 2):
            distY = a[0] - b[0]
            distX = a[1] - b[1]
            gcd = math.gcd(distX, distY)
            distY = distY // gcd
            distX = distX // gcd

            i = 0
            while True:
                aa = (a[0] + distY * i, a[1] + distX * i)
                bb = (b[0] - distY * i, b[1] - distX * i)

                aa_in = aa[0] in indicies and aa[1] in indicies
                bb_in = bb[0] in indicies and bb[1] in indicies

                if aa_in:
                    antinodes.add(aa)
                if bb_in:
                    antinodes.add(bb)
                if not aa_in and not bb_in:
                    break
                i += 1

    return len(antinodes)

part1 = solve1()
part2 = solve2()

print(part1)
print(part2)
