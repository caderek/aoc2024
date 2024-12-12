from itertools import product

with open('input.txt') as file:
    input = file.read().strip()

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
dirs_all = (*dirs, (-1, -1), (-1, 1), (1, 1), (1, -1))

def create_graph(grid, edge_condition):
    graph = {}
    for y, x in product(indicies, repeat=2):
        val = grid[y][x]
        node = (y, x)
        if node not in graph:
            graph[node] = []
        for dy, dx in dirs:
            y2 = y + dy
            x2 = x + dx
            if y2 in indicies and x2 in indicies:
                val2 = grid[y2][x2]
                if edge_condition(val, val2):
                    graph[node].append((y2, x2))
    return graph

def find_components(graph):
    def dfs(graph, node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, component)

    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    return components

def count_vertices(points):
    all_points = set()

    for y, x in points:
        # expand each point into 3x3 grid of points
        # so we can identify all vertices by counting neighbors
        cell_points = (
            (y * 2, x * 2),
            (y * 2 + 1, x * 2),
            (y * 2 + 2, x * 2),
            (y * 2, x * 2 + 1),
            (y * 2, x * 2 + 2),
            (y * 2 + 1, x * 2 + 1),
            (y * 2 + 2, x * 2 + 2),
            (y * 2 + 1, x * 2 + 2),
            (y * 2 + 2, x * 2 + 1),
        )

        for v in cell_points:
            all_points.add(v)

    vertices = 0

    for y, x in all_points:
        diagonal_neighbors = 0
        all_neighbors = 0

        for dy, dx in dirs_all:
            if (y + dy, x + dx) in all_points:
                all_neighbors += 1
                if dx != 0 and dy != 0:
                    diagonal_neighbors += 1
        
        if all_neighbors == 3 or (all_neighbors == 7 and diagonal_neighbors == 3):
            vertices += 1
        elif all_neighbors == 6 and diagonal_neighbors == 2:
            vertices += 2

    return vertices

def isolate_region(points):
    min_y = min([y for y, _ in points])
    min_x = min([x for _, x in points])
    h = max([y for y, _ in points]) - min_y + 1
    w = max([x for _, x in points]) - min_x + 1
    region = [['.' for _ in range(w + 1)] for _ in range(h + 1)]

    for y, x in points:
        region[y - min_y][x - min_x] = 'O'

    return region

def count_fences(grid):
    h = len(grid)
    w = len(grid[0])
    fences = 0

    for y in range(h):
        prev = '.'
        for x in range(w):
            if grid[y][x] != prev:
                fences += 1
                prev = grid[y][x]

    for x in range(w):
        prev = '.'
        for y in range(h):
            if grid[y][x] != prev:
                fences += 1
                prev = grid[y][x]

    return fences

lines = input.splitlines()
size = len(lines)

farm = [list(line) for line in lines]
indicies = set(range(len(farm)))
plants = set(''.join(lines))

graph = create_graph(farm, lambda a, b: a == b)
regions = find_components(graph)

part1 = 0
part2 = 0

for points in regions:
    region = isolate_region(points)
    area = len(points)
    perimeter = count_fences(region)
    sides = count_vertices(points)
    part1 += area * perimeter
    part2 += area * sides

print(part1)
print(part2)

