import math
import re
from itertools import product

with open('input.txt') as file:
    input = [
        [int(x) for x in re.findall("\d+", line)]
        for line in  file.read().strip().splitlines()
    ]

calc = (
    lambda a, b: a + b,
    lambda a, b: a * b,
    lambda a, b: a * 10 ** (math.ceil(math.log10(b+1))) + b,
)

def solve(symbols):
    sum = 0

    for left, *nums in input:
        l = len(nums) - 1
        indicies = range(l)
        for ops in product(symbols, repeat=l):
            right = nums[0]
            for i in indicies:
                if right > left:
                    continue
                right = calc[ops[i]](right, nums[i + 1])
            if left == right:
                sum += left
                break
    return sum

part1 = solve((0, 1))
part2 = solve((0, 1, 2))

print(part1)
print(part2)

