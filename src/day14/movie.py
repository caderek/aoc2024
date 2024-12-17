from manim import *
from statistics import stdev
from itertools import pairwise
from copy import deepcopy
import re
import json
from collections import defaultdict
from functools import cmp_to_key


with open('input.txt') as file:
    input = file.read().strip()

with open('robots.json') as json_data:
    robots_data = json.load(json_data)

robots_info = defaultdict(lambda: { "color": "#ffffff", "layer": 0 })

for id, data in robots_data:
    robots_info[id] = data

def compare(a, b):
    return robots_info[a[4]]["layer"] - robots_info[b[4]]["layer"]

w, h = 101, 103
robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in input.splitlines()]
robots = [[val[0], val[1], val[2], val[3], str(i).rjust(3, '0') ] for i, val in enumerate(robots)]
robots.sort(key=cmp_to_key(compare))

def draw(robots):
    grid = [[' ' for x in range(w)] for y in range(h)]
    for x, y, _, _, _ in robots:
        grid[y][x] = '#'
    for line in grid:
        print(''.join(line))

def draw2(robots):
    grid = [[' ' * 4 for x in range(31)] for y in range(33)]
    for x, y, _, _, id in robots:
        xx = x - 20
        yy = y - 47
        if xx in range(31) and yy in range(33):
            grid[yy][xx] = f"{id} "
    for line in grid:
        print(''.join(line))


def simulate(robots, time):
    for i, robot  in enumerate(robots):
        x, y, vx, vy, _ = robot
        robots[i][0] = (x + vx * time) % w
        robots[i][1] = (y + vy * time) % h

special_target = (35,52)
target = 8168 # + 103*101 * 4 

star_id = '232'

config.pixel_height = h * 10
config.pixel_width = w * 10
config.frame_height = h
config.frame_width = w

class StarWasBorn(Scene):
    def construct(self):
        self.camera.background_color = 0x0f0f15
        self.start_y = h // 2
        self.start_x = w // 2
        self.size = 1

        simulate(robots, target - 10)
        items = None

        for sec in range(1, 11):
            if items:
                self.remove(*items)
            simulate(robots, 1)
            items = [self.get_robot(x, y, id) for x, y, _, _, id in robots]
            self.add(*items)
            self.wait(0.1)

        self.wait(5)
    
    def get_robot(self, x, y, id):
        el = Circle(0.8)
        el.set_stroke(width=0)
        el.set_fill(robots_info[id]["color"], opacity=1)
        el.shift(UP * self.start_y)
        el.shift(LEFT * self.start_x)
        el.shift(DOWN * y * self.size)
        el.shift(RIGHT * x * self.size)

        return el
