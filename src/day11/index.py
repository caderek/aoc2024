from functools import cache

with open('input.txt') as file:
    input = file.read().strip()

nums = [int(x) for x in input.split(' ')]

def solve(max_depth):
    @cache # part 2 optimization
    def rec(n, depth = 0):
        if depth == max_depth:
            return 1
        depth += 1
        if n == 0:
            return rec(1, depth)
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            return rec(int(s[:l//2]), depth) + rec(int(s[l//2:]), depth)
        return rec(n * 2024, depth)
    
    return sum(rec(n) for n in nums)

part1 = solve(25)
part2 = solve(75)

print(part1)
print(part2)
