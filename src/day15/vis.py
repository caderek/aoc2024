import sys
import math
from manim import *
from itertools import chain, pairwise
from copy import deepcopy
from collections import defaultdict, deque

with open('input.txt') as file:
    input = file.read().strip()

# input = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########
#
# <^^>>>vv<v>>v<<"""

# input = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######
#
# <vv<<^^<<^^"""

input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

dirs = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

def find_start(wh):
    for y in range(len(wh)):
        for x in range(len(wh[0])):
            if wh[y][x][0] == '@':
                return (y, x)

def sum_coords(wh, sym):
    res = 0
    for y in range(len(wh)):
        for x in range(len(wh[0])):
            if wh[y][x][0] == sym:
                res += 100 * y + x
    return res

def double(cell):
    if cell == '@':
        return ['@', '.']
    if cell == 'O':
        return ['[', ']']
    return [cell, cell]

def expand_warehouse(wh):
    return [list(chain(*[double(cell) for cell in row])) for row in wh]

def add_ids(wh):
    ids = set()
    for y in range(len(wh)):
        for x in range(len(wh[0])):
            wh[y][x] = (wh[y][x], complex(y, x))
            ids.add(complex(y, x))
    return ids

def solve1(w, move, start):
    ry, rx = start
    moved = False

    dy, dx = dirs[move]
    yy, xx = ry + dy, rx + dx
    if w[yy][xx][0] == '#':
        pass
    elif w[yy][xx][0] == '.' or solve1(w, move, (yy, xx)):
        w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
        ry, rx = yy, xx
        moved  = True

    return moved

def solve2(w, move, start):
    ry, rx = start
    moved = False

    dy, dx = dirs[move]
    yy, xx = ry + dy, rx + dx
    if w[yy][xx][0] == '#':
        pass
    elif (
        w[yy][xx][0] == '.' or
        (move in ['<', '>'] and solve2(w, move, (yy, xx)))
    ):
        w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
        ry, rx = yy, xx
        moved = True
    elif move in ['^', 'v']:
        side_dir = 1 if w[yy][xx][0] == '[' else -1
        w_copy = deepcopy(w)
        side1_moved = solve2(w_copy, move, (yy, xx))
        side2_moved = solve2(w_copy, move, (yy, xx + side_dir))

        if side1_moved and side2_moved:
            solve2(w, move, (yy, xx))
            solve2(w, move, (yy, xx + side_dir))
            w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
            ry, rx = yy, xx
            moved = True

    return moved

raw_warehouse, raw_moves = input.split('\n\n')

warehouse = [[*line] for line in raw_warehouse.splitlines()]
expanded = expand_warehouse(deepcopy(warehouse))

moves = [*"".join(raw_moves.splitlines())]

####################################################################

colors = {
    '_': 0x13100F,
    '.': 0x473C3A,
    '#': 0x2D2321,
    '@': 0xfa3939,
    'O': 0xDF8E48,
    '[': 0xDF8E48,
}

def shortest_path_bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (current_node, path) = queue.popleft()

        if current_node == end:
            return path
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # Return None if no path is found


def get_shortest_path(idle_steps):
    graph = defaultdict(set)

    for a, b in pairwise(idle_steps):
        graph[a].add(b)
        graph[b].add(a)

    return shortest_path_bfs(graph, idle_steps[0], idle_steps[-1])

def get_positions(wh):
    positions = {}
    robot_pos = None
    for y in range(len(wh)):
        for x in range(len(wh[0])):
            val = wh[y][x]
            if val[0] in ['O', '@', '[', ']']:
                positions[val[1]] = complex(y, x)
            if val[0] == '@':
                robot_pos = complex(y, x)
    return positions , robot_pos

def scaled_sigmoid(n, k=0.1, n0=50):
    return 0.9 / (1 + math.exp(-k * (n - n0))) + 0.1

def get_cell(self, y, x, val):
    color = colors[val]

    if val == '#':
        el = Square(side_length=1)
    elif val == '[':
        el = RoundedRectangle(width=1.9, height=0.9, corner_radius=0.1)
        el.shift(RIGHT * 0.5)
    elif val == 'O':
        el = RoundedRectangle(width=0.9, height=0.9, corner_radius=0.1)
    else:
        el = Circle(0.45)

    el.set_stroke(width=0)
    el.set_fill(color, opacity=1)
    el.shift(UP * self.start_y)
    el.shift(LEFT * self.start_x)
    el.shift(DOWN * y * self.size)
    el.shift(RIGHT * x * self.size)
    return el

def play(self, h, w, wh, solve, sym):
    self.camera.background_color = colors['_']
    self.start_y = h / 2 - 0.5
    self.start_x = w / 2 - 0.5
    self.size = 1
    wait_before = 1
    wait_after = 3

    floor = Rectangle(height=len(wh), width=len(wh[0]))
    floor.set_stroke(width=0)
    floor.set_fill(colors['.'], opacity=1)

    self.add(floor)

    add_ids(wh)

    boxes = {}
    walls = []
    robot = None

    for y in range(len(wh)):
        for x in range(len(wh[0])):
            val = wh[y][x][0]
            if val in ['O', '@', '[']:
                boxes[wh[y][x][1]] = get_cell(self, y, x, val)
                if val == '@':
                    robot = boxes[wh[y][x][1]]
            elif val == '#':
                walls.append(get_cell(self, y, x, val))

    self.add(*walls)
    self.add(*boxes.values())

    prev_positions, prev_robot_pos = get_positions(wh)

    self.wait(wait_before)

    idle_steps = [prev_robot_pos]

    parts = 0

    for move in moves:
        moved = solve(wh, move, find_start(wh))
        if moved:
            curr_positions, curr_robot_pos = get_positions(wh)
            moved_boxes = []
            dir = None

            for key, box in boxes.items():
                if prev_positions[key] != curr_positions[key]:
                    if not dir:
                        dy = prev_positions[key].real - curr_positions[key].real
                        dx = prev_positions[key].imag - curr_positions[key].imag
                        dir = complex(dy, dx)
                    moved_boxes.append(box)

            moved_count = len(moved_boxes)

            dy, dx = dir.real, dir.imag
            shift = UP * dy if dy != 0 else LEFT * dx

            if moved_count > 1:
                if len(idle_steps) > 1:
                    idle_path = get_shortest_path(idle_steps)
                    for a, b in pairwise(idle_path):
                        sdy = a.real - b.real
                        sdx = a.imag - b.imag
                        sshift = UP * sdy if sdy != 0 else LEFT * sdx
                        self.play(robot.animate.shift(sshift), rate_func=rate_functions.linear, run_time=0.05)
                        parts += 1
                time = scaled_sigmoid(moved_count)
                self.play(Group(*moved_boxes).animate.shift(shift), rate_func=rate_functions.smooth, run_time=time)
                idle_steps = [curr_robot_pos]
                parts += 1
            else:
                idle_steps.append(curr_robot_pos)
                # moved_boxes[0].shift(shift)
                # pass
            prev_positions = curr_positions
        # if parts > 3:
        #     break

    self.wait(wait_after)
    print('PARTS:', parts)
    print('Result:', sum_coords(wh, sym))



h = len(warehouse)
w = len(warehouse[0])
cell_size = 18 * 5
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / cell_size
config.frame_width = config.pixel_width / cell_size

class Day15A(Scene):
    def construct(self):
        play(self, h, w, warehouse, solve1, 'O')

# h = len(expanded)
# w = len(expanded[0])
# cell_size = 18 * 5
# config.pixel_height = 1080
# config.pixel_width = 1920
# config.frame_height = config.pixel_height / cell_size
# config.frame_width = config.pixel_width / cell_size
#
# class Day15B(Scene):
#     def construct(self):
#         play(self, h, w, expanded, solve2, '[')
