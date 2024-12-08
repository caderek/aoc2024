import math
from itertools import combinations, product

with open('input.txt') as file:
    input = [[*line] for line in file.read().strip().splitlines()]

indicies = set(product(range(len(input)), repeat=2))
antennas = {}

for y, x in indicies:
    val = input[y][x]
    if val != '.':
        antennas.setdefault(val, []).append((y, x))

def get_point():
    return

def solve1():
    antinodes = set()

    for coords in antennas.values():
        for [ay, ax], [by, bx] in combinations(coords, 2):
            dy = ay - by
            dx = ax - bx

            aa = (ay + dy, ax + dx)
            bb = (by - dy, bx - dx)

            if aa in indicies:
                antinodes.add(aa)
            if bb in indicies:
                antinodes.add(bb)

    return len(antinodes)

def solve2():
    antinodes = set()

    for coords in antennas.values():
        for [ay, ax], [by, bx] in combinations(coords, 2):
            dy = ay - by
            dx = ax - bx
            gcd = math.gcd(dx, dy)
            dy = dy // gcd
            dx = dx // gcd

            i = 0
            while True:
                aa = (ay + dy * i, ax + dx * i)

                if aa in indicies:
                    antinodes.add(aa)
                    i += 1
                else:
                    break

            i = 0
            while True:
                bb = (by - dy * i, bx - dx * i)

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
