import re

with open('input.txt') as file:
    input = file.read().strip()

def solve(machine, shift = 0):
    [ax, ay, bx, by, px, py] = machine
    px += shift
    py += shift

    a = (py * bx - px * by) / (ay * bx - ax * by)
    b = -((py * ax - px * ay) / (ay * bx - ax * by))

    return int(a * 3 + b) if a.is_integer() and b.is_integer() else 0

machines = [[int(x) for x in re.findall("\d+", p)] for p in input.split('\n\n')]

part1 = sum(solve(machine) for machine in machines)
part2 = sum(solve(machine, 10000000000000) for machine in machines)

print(part1)
print(part2)

