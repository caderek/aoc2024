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
        for ops in product(symbols, repeat=len(nums) - 1):
            right = nums[0]
            for i in range(1, len(nums)):
                if right > left:
                    continue
                right = calc[ops[i - 1]](right, nums[i])
            if left == right:
                sum += left
                break
    return sum

part1 = solve((0, 1))
part2 = solve((0, 1, 2))

print(part1)
print(part2)

