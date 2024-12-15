from itertools import chain
from copy import deepcopy

with open('input.txt') as file:
    input = file.read().strip()

dirs = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

def find_start(w):
    for y in range(len(w)):
        for x in range(len(w[0])):
            if expanded[y][x] == '@':
                return (y, x)

def sum_coords(w, sym):
    res = 0
    for y in range(len(w)):
        for x in range(len(w[0])):
            if w[y][x] == sym:
                res += 100 * y + x
    return res

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

    return moved

def solve2(w, moves, start):
    ry, rx = start
    moved = False

    for i, move in enumerate(moves):
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
        elif move in ['^', 'v']:
            # Check if both sides of the box can move
            # before applying change to the main grid
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

    return moved

raw_warehouse, raw_moves = input.split('\n\n')

warehouse = [[*line] for line in raw_warehouse.splitlines()]
expanded = expand_warehouse(deepcopy(warehouse))

moves = [*"".join(raw_moves.splitlines())]

solve1(warehouse, moves, find_start(warehouse))
solve2(expanded, moves, find_start(expanded))

print(sum_coords(warehouse, 'O'))
print(sum_coords(expanded, '['))

