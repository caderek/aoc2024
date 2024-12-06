with open('input.txt') as file:
    input = [[*x] for x in file.read().strip().splitlines()]

h = len(input)
w = len(input[0])
start = next(
    (i, j) for i, row in enumerate(input)
    for j, element in enumerate(row) if element == '^'
)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solve1(grid):
    visited = {start}
    dir = 0
    prev = start

    while True:
        dy, dx = dirs[dir]
        next = (prev[0] + dy, prev[1] + dx)

        if next[0] < 0 or next[1] < 0 or next[0] >= h or next[1] >= w:
            break

        val = grid[next[0]][next[1]]

        if val == '#':
            dir = (dir + 1) % len(dirs)
        else:
            visited.add(next)
            prev = next

    return visited

def does_loop(grid):
    steps = set()
    dir = 0
    prev = start

    while True:
        dy, dx = dirs[dir]
        next = (prev[0] + dy, prev[1] + dx)

        if next[0] < 0 or next[1] < 0 or next[0] >= h or next[1] >= w:
            return False

        val = grid[next[0]][next[1]]

        if val == '#':
            dir = (dir + 1) % len(dirs)
        elif prev + next in steps:
            return True
        else:
            steps.add(prev + next)
            prev = next

def solve2(input, visited):
    loops = 0

    for y, x in visited:
        val = input[y][x]
        
        if val != '.':
            continue

        input[y][x] = '#'

        if does_loop(input):
            loops += 1

        input[y][x] = val

    return loops


visited = solve1(input)
part1 = len(visited)
part2 = solve2(input, visited)

print(part1)
print(part2)

