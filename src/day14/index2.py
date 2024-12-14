import os
import time
import re

with open('input.txt') as file:
    input = file.read().strip()

w = 101
h = 103

# input = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""
# w = 11
# h = 7

robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in input.splitlines()]

print('len:', len(robots))
t = 0

def print_tree(robots):
    grid = []
    for y in range(h):
        grid.append([])
        for x in range(w):
            grid[y].append(' ')


    for robot in robots:
        grid[robot[1]][robot[0]] = '#'

    vline = 0

    for y in range(h):
        item = grid[y][50]
        if grid[y][50] == '#':
            vline+=1


    if vline > 30:
        for line in grid:
            print(''.join(line))
        print(t)
        time.sleep(0.1)



def is_tree(robots):
    points = set([(robot[0], robot[1]) for robot in robots])
    lines = []
    mid = w // 2
    i = 0

    for y in range(h-1):
        for x in range(mid - i, mid + i + 1):
            if (x, y) not in points:
              return False

    if (mid, h-1) not in points:
        return False

    return True
        


print_tree(robots)

while True:
    # print(time)
    for i, robot  in enumerate(robots):
        x, y, vx, vy = robot
        robots[i][0] = (x + vx) % w
        robots[i][1] = (y + vy) % h
    t += 1
    print_tree(robots)
    # time.sleep(0.01)
    # os.system('clear')


print('time:', t)
    
# a = 0
# b = 0
# c = 0
# d = 0
# for x, y, _, __ in robots:
#     if x in range(w//2) and y in range(h//2):
#         a += 1
#     if x in range(w//2) and y in range(h//2 + 1, h):
#         b += 1
#     if x in range(w//2 +1, w) and y in range(h//2 + 1, h):
#         c += 1
#     if x in range(w//2 +1, w) and y in range(h//2):
#         d += 1
#
# print(a * b * c * d)
#
#
