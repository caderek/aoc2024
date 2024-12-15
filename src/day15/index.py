import sys
import re
from itertools import chain
from copy import deepcopy

sys.setrecursionlimit(1000000)

with open('input.txt') as file:
    input = file.read().strip()

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

input = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

dirs = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

def sum_coords(w, sym):
    res = 0
    for y in range(len(w)):
        for x in range(len(w[0])):
            if w[y][x] == sym:
                res += 100 * y + x
    return res

def pprint(grid):
    for line in grid:
        print(''.join(line))
    print('-' * len(grid))

def double(cell):
    if cell == '@':
        return ['@', '.']
    if cell == 'O':
        return ['[', ']']
    return [cell, cell]

def expand_warehouse(w):
    return [list(chain(*[double(cell) for cell in row])) for row in w]

def solve1(w, moves, start):
    ry, rx = start
    moved = False

    for move in moves:
        dy, dx = dirs[move]
        yy, xx = ry + dy, rx + dx
        if w[yy][xx] == '#':
            pass
        elif w[yy][xx] == '.' or solve1(w, [move], (yy, xx)):
            w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
            ry, rx = yy, xx
            moved = True

        # print('Move:', move)
        # pprint(w)

    return moved

def solve2(w, moves, start, main = False):
    ry, rx = start
    moved = False

    for move in moves:
        dy, dx = dirs[move]
        yy, xx = ry + dy, rx + dx
        if w[yy][xx] == '#':
            pass
        elif (
            w[yy][xx] == '.' or
            (move in ['<', '>'] and solve2(w, [move], (yy, xx)))
        ):
            w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
            ry, rx = yy, xx
            moved = True
        else:
            side_dir = 1 if w[yy][xx] == '[' else -1
            w_copy = deepcopy(w)
            side1_moved = solve2(w_copy, [move], (yy, xx))
            side2_moved = solve2(w_copy, [move], (yy, xx + side_dir))

            if side1_moved and side2_moved:
                solve2(w, [move], (yy, xx))
                solve2(w, [move], (yy, xx + side_dir))
                w[yy][xx], w[ry][rx] = w[ry][rx], w[yy][xx]
                ry, rx = yy, xx
                moved = True

        if main:
            print('Move:', move)
            pprint(w)

    return moved

a, b = input.split('\n\n')

warehouse = [[*line] for line in a.splitlines()]
expanded = expand_warehouse(deepcopy(warehouse))

moves = [*"".join(b.splitlines())]

start1 = None

for y in range(len(warehouse)):
    for x in range(len(warehouse[0])):
        if warehouse[y][x] == '@':
            start1 = (y, x)

start2 = None

for y in range(len(expanded)):
    for x in range(len(expanded[0])):
        if expanded[y][x] == '@':
            start2 = (y, x)

pprint(warehouse)
pprint(expanded)

solve1(warehouse, moves, start1)
solve2(expanded, moves, start2, True)

print(sum_coords(warehouse, 'O'))
print(sum_coords(expanded, '['))

