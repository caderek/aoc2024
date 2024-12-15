# from manim import *
from statistics import stdev
from itertools import pairwise
from copy import deepcopy
import re

with open('input.txt') as file:
    input = file.read().strip()

w, h = 101, 103
robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in input.splitlines()]
robots = [[x, y, vx, vy, (x, y)] for x, y, vx, vy in robots]

def draw(robots):
    grid = [[' ' for x in range(w)] for y in range(h)]
    for x, y, _, __, ___ in robots:
        grid[y][x] = '#'
    for line in grid:
        print(''.join(line))

def simulate(robots, time):
    for i, robot  in enumerate(robots):
        x, y, vx, vy, _ = robot
        robots[i][0] = (x + vx * time) % w
        robots[i][1] = (y + vy * time) % h

special_target = (35,52)
target = 8168

simulate(robots, target)
draw(robots)
print(robots[0])

special = [x for x in robots if x[0] == special_target[0] and x[1] == special_target[1]][0]

print('special:', special)

# config.pixel_height = h * 10
# config.pixel_width = w * 10
# config.frame_height = h
# config.frame_width = w
#
# class Day14(Scene):
#     def construct(self):
#         self.camera.background_color = 0x0f0f15
#         self.start_y = h // 2
#         self.start_x = w // 2
#         self.size = 1
#
#         simulate(robots, part2 - 10)
#
#         for sec in range(1, 20):
#             simulate(robots, 1)
#             items = [self.get_point(y, x, 0.4, 0xff3355, 1) for x, y, _, __ in robots]
#             self.add(*items)
#             time = 1 if sec == 10 else 0.1
#             self.wait(time)
#             self.remove(*items)
#
#     def get_point(self, y, x, radius, color, opacity):
#         el = Circle(radius)
#         el.set_stroke(width=0)
#         el.set_fill(color, opacity=opacity)
#         el.shift(UP * self.start_y)
#         el.shift(LEFT * self.start_x)
#         el.shift(DOWN * y * self.size)
#         el.shift(RIGHT * x * self.size)
#
#         return el
