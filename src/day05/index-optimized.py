from functools import cmp_to_key
from itertools import pairwise

with open('input.txt') as file:
    rules_raw, manuals_raw = file.read().split('\n\n')
    rules = set(rules_raw.splitlines())
    manuals = [line.split(',') for line in manuals_raw.splitlines()]

def compare(a, b):
    return -1 if f"{a}|{b}" in rules else 0

key = cmp_to_key(compare)

def is_sorted(manual):
    return all(compare(a, b) == -1 for a, b in pairwise(manual))

def sorted_pages(manual):
    return sorted(manual, key=key)

def get_mid(items):
    return int(items[len(items) // 2])

part1 = 0
part2 = 0

for m in manuals:
    if is_sorted(m):
        part1 += get_mid(m)
    else:
        part2 += get_mid(sorted_pages(m))

print(part1)
print(part2)

