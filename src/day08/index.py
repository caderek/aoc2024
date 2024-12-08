import math
from itertools import combinations, product

with open('input.txt') as file:
    input = [[*line] for line in file.read().strip().splitlines()]

size = len(input)
indicies = set(product(range(size), repeat=2))
antennas = {}

for y, x in indicies:
    val = input[y][x]
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

            if aa in indicies:
                antinodes.add(aa)
            if bb in indicies:
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

                if aa in indicies:
                    antinodes.add(aa)
                    i += 1
                else:
                    break

            i = 0
            while True:
                bb = (b[0] - distY * i, b[1] - distX * i)

                if bb in indicies:
                    antinodes.add(bb)
                    i += 1
                else:
                    break

    return len(antinodes)

part1 = solve1()
part2 = solve2()

print(part1)
print(part2)
