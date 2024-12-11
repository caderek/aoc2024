import functools

with open('input.txt') as file:
    input = file.read().strip()

nums = [int(x) for x in input.split(' ')]

def solve(max):
    @functools.lru_cache(maxsize=None)
    def recur(n, d = 0):
        if d == max:
            return 1
        d = d +1
        if n == 0:
            return recur(1, d)
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            return recur(int(s[:l//2]), d) + recur(int(s[l//2:]), d)
        return recur(n * 2024, d)
    
    return sum(recur(x) for x in nums)

part1 = solve(25)
part2 = solve(75)

print(part1)
print(part2)
