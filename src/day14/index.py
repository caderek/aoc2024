from statistics import stdev
from itertools import pairwise
from copy import deepcopy
import re

with open('input.txt') as file:
    input = file.read().strip()

w, h = 101, 103
robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in input.splitlines()]

def draw(robots):
    grid = [[' ' for x in range(w)] for y in range(h)]
    for x, y, _, __ in robots:
        grid[y][x] = '#'
    for line in grid:
        print(''.join(line))

def simulate(robots, time):
    for i, robot  in enumerate(robots):
        x, y, vx, vy = robot
        robots[i][0] = (x + vx * time) % w
        robots[i][1] = (y + vy * time) % h

def get_safety_factor(robots):
    a, b, c, d = 0, 0, 0 ,0

    for x, y, _, __ in robots:
        if x in range(w//2) and y in range(h//2):
            a += 1
        if x in range(w//2) and y in range(h//2 + 1, h):
            b += 1
        if x in range(w//2 +1, w) and y in range(h//2 + 1, h):
            c += 1
        if x in range(w//2 +1, w) and y in range(h//2):
            d += 1

    return a * b * c * d

def dist_stdev(nums):
    nums.sort()
    distances = [abs(a - b) for a, b in pairwise(nums)]
    return stdev(distances)

def get_order_score(robots):
    dev_h = dist_stdev([robot[0] for robot in robots])
    dev_v = dist_stdev([robot[1] for robot in robots])
    return dev_h + dev_v

def solve1(robots):
    simulate(robots, 100)
    return get_safety_factor(robots)

def solve2(robots, max_time):
    max_order = 0 
    max_order_sec = 0

    for sec in range(1, max_time):
        simulate(robots, 1)
        order_score = get_order_score(robots)
        if order_score > max_order:
            max_order = order_score
            max_order_sec = sec

    return max_order_sec

part1 = solve1(deepcopy(robots))
part2 = solve2(deepcopy(robots), max_time = w * h)

# confirm visually
simulate(robots, part2)
draw(robots)

print(part1)
print(part2)

