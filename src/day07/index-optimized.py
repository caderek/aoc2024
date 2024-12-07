import math
import re
from itertools import product

with open('input.txt') as file:
    input = [
        [int(x) for x in re.findall("\d+", line)]
        for line in  file.read().strip().splitlines()
    ]

calc = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '.': lambda a, b: a * 10 ** (math.ceil(math.log10(b+1))) + b,
}

def solve(symbols):
    sum = 0

    for left, *nums in input:
        first, *rest = nums
        for ops in product(symbols, repeat=len(rest)):
            right = first
            for op, num in zip(ops, rest):
                if right > left:
                    continue
                right = calc[op](right, num)
            if left == right:
                sum += left
                break
    return sum

part1 = solve('+*')
part2 = solve('+*.')

print(part1)
print(part2)

