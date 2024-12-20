import re

with open('input.txt') as file:
    mem = file.read()

to_match = r"mul\(\d{1,3},\d{1,3}\)"
to_skip = r"don't\(\)[\s\S]*?(do\(\)|$)"

def calc(mem):
    return sum(
        int(a) * int(b) for a, b
        in [re.findall(r"\d+", mul) for mul in re.findall(to_match, mem)]
    )

part1 = calc(mem)
part2 = calc(re.sub(to_skip, ' ', mem))

print(part1)
print(part2)
