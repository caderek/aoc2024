import re

with open('src/day01/input.txt', 'r') as file:
    items = [re.split(r'\s+', line.strip()) for line in file]

