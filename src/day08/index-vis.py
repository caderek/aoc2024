import math
from itertools import combinations, product
from manim import *


with open('input.txt') as file:
    input = [[*line] for line in file.read().strip().splitlines()]

indicies = set(product(range(len(input)), repeat=2))
antennas = {}

for y, x in indicies:
    val = input[y][x]
    if val != '.':
        antennas.setdefault(val, []).append((y, x))

def solve1():
    antinodes = set()

    for i, coords in enumerate(antennas.values()):
        for [ay, ax], [by, bx] in combinations(coords, 2):
            dy = ay - by
            dx = ax - bx

            aa = (ay + dy, ax + dx)
            bb = (by - dy, bx - dx)

            if aa in indicies:
                antinodes.add(aa)
                yield aa, i
            if bb in indicies:
                antinodes.add(bb)
                yield bb, i

    return len(antinodes)

def solve2():
    antinodes = set()

    for j, coords in enumerate(antennas.values()):
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
                    yield aa, j
                    i += 1
                else:
                    break

            i = 0
            while True:
                bb = (by - dy * i, bx - dx * i)

                if bb in indicies:
                    antinodes.add(bb)
                    yield bb, j
                    i += 1
                else:
                    break

    return len(antinodes)

class Day8(Scene):
    def construct(self):
        self.camera.background_color = 0x15161e
        self.size = 8 / len(input)
        self.start = 4 - self.size / 2

        bg = Square(8)
        bg.set_stroke(width=0)
        bg.set_fill(0x0f0f15, opacity=1)
        self.add(bg)

        colors = [
            ManimColor.from_hsv((i / len(antennas.values()), 0.7, 0.7))
            for i, _ in enumerate(antennas.values())
        ]

        self.add(*[self.get_point(y, x, 0.005, WHITE, opacity=1) for y, x in indicies])

        for i, coords in enumerate(antennas.values()):
            for y, x in coords:
                antenna = self.get_antenna(y, x, colors[i], opacity=1)
                self.add(antenna)

        antinodes = {}

        for [y, x], i in solve1():
            item = self.get_point(y, x, self.size / 4, colors[i], opacity = 0.5)
            antinodes.setdefault(i, []).append(item)

        for group in antinodes.values():
            self.play(
                LaggedStart(
                    *[GrowFromCenter(x, rate_func=rate_functions.ease_out_back, run_time=0.2) for x in group],
                    lag_ratio=0.05
                )
            )

        self.wait(2)
        for group in antinodes.values():
            self.remove(*group)
        self.wait(1)

        antinodes = {}

        for [y, x], i in solve2():
            item = self.get_point(y, x, self.size / 4, colors[i], opacity = 0.5)
            antinodes.setdefault(i, []).append(item)

        for group in antinodes.values():
            self.play(
                LaggedStart(
                    *[GrowFromCenter(x, rate_func=rate_functions.ease_out_back, run_time=0.2) for x in group],
                    lag_ratio=0.05
                )
            )

        self.wait(2)

    def get_antenna(self, y, x, color, opacity):
        el = SVGMobject('antenna.svg', width=self.size * 0.8)

        el.set_stroke(width=0)
        el.set_fill(color, opacity=opacity)
        el.shift(UP * self.start)
        el.shift(LEFT * self.start)
        el.shift(DOWN * y * self.size)
        el.shift(RIGHT * x * self.size)

        return el

    def get_point(self, y, x, radius, color, opacity):
        el = Circle(radius)
        el.set_stroke(width=0)
        el.set_fill(color, opacity=opacity)
        el.shift(UP * self.start)
        el.shift(LEFT * self.start)
        el.shift(DOWN * y * self.size)
        el.shift(RIGHT * x * self.size)

        return el
