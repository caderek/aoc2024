from functools import cmp_to_key

with open('input.txt') as file:
    rules_raw, manuals_raw = file.read().split('\n\n')
    rules = set(rules_raw.splitlines())
    manuals = [
        [int(x) for x in line.split(',')]
        for line in manuals_raw.splitlines()
    ]

def compare(a, b):
    return -1 if f"{a}|{b}" in rules else 0

key = cmp_to_key(compare)

def sorted_pages(manual):
    return sorted(manual, key=key)

def get_mid(items):
    return items[len(items) // 2]

part1 = sum(get_mid(m) for m in manuals if sorted_pages(m) == m)
part2 = sum(get_mid(m) for m in map(sorted_pages, manuals)) - part1

print(part1)
print(part2)

