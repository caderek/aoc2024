import itertools

with open('src/day02/input.txt', 'r') as file:
    items = [[int(x) for x in line.split()] for line in file]

def isSafe(levels):
    steps = [a - b for a, b in itertools.pairwise(levels)]
    return all(x > 0 and x < 4 for x in steps) or all(x < 0 and x > -4 for x in steps)

def isAnySubsetSafe(levels):
    subsets = [levels[:i] + levels[i+1:] for i in range(len(levels))]
    return any(isSafe(subset) for subset in subsets)


part1 = sum(1 for levels in items if isSafe(levels))
part2 = sum(1 for levels in items if isAnySubsetSafe(levels))

print(part1)
print(part2)
