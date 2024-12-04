with open('src/day04/input.txt', 'r') as file:
    input = [line.strip() for line in file]

def solve(data, slices, variants):
    count = 0

    for x in range(len(data[0])):
        for y in range(len(data)):
            for slice in slices:
                try:
                    word =  ''.join([data[y + dY][x + dX] for dX, dY in slice])

                    if word in variants:
                        count += 1
                except:
                    pass

    return count

slices1 = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 1), (2, 2), (3, 3)),
    ((0, 3), (1, 2), (2, 1), (3, 0)),
]

slices2 = [
    ((0, 0), (1, 1), (2, 2), (0, 2), (1, 1), (2, 0)),
]

part1 = solve(input, slices1, {'XMAS', 'SAMX'})
part2 = solve(input, slices2, {'MASMAS', 'SAMSAM', 'MASSAM', 'SAMMAS'})

print(part1)
print(part2)
