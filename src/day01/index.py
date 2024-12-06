import re

a = []
b = []

with open('input.txt') as file:
    items = [re.split(r'\s+', line.strip()) for line in file]

    for item in items:
        a.append(int(item[0]))
        b.append(int(item[1]))

a.sort()
b.sort()

distances = [abs(x - y) for x, y in zip(a, b)]

occurences = {}

for y in b:
    if y in occurences:
        occurences[y] += 1
    else:
        occurences[y] = 1

scores = [x * occurences.get(x, 0) for x in a]

print(sum(distances))
print(sum(scores))
