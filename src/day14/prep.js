import fs from 'node:fs'

const robotsRaw = fs.readFileSync('tree.txt', {encoding: 'utf8'}).trim()
const colorsRaw = fs.readFileSync('tree-hex.txt', {encoding: 'utf8'}).trim()

const COLORS_MAP = {
  '#ffff00': '#ffff00',
  '#00aa00': '#00aa00',
  '#009900': '#009900',
  '#008800': '#008800',
  '#007700': '#007700',
  '#006600': '#006600',
  '#005500': '#005500',
  '#004400': '#004400',
  '#003300': '#003300',
  '#ff0000': '#ff0000',
  '#ff00ff': '#ff00ff',
  '#ff7700': '#ff7700',
  '#00ffff': '#00ffff',
  '#503525': '#503525',
  '#593a29': '#593a29',
  '#704933': '#704933',
  '#8b5a3f': '#8b5a3f'
}

const REVERSE_COLOR_MAP = Object.fromEntries(
  Object.entries(COLORS_MAP).map(([a, b]) => [b, a])
)

const SPECIAL_LAYERS = {
  '#ffff00': 200, 
  '#ff0000': 190,
  '#00ffff': 190,
  '#ff00ff': 180,
  '#ff7700': 180,
}

const colors = colorsRaw
  .split('\n')
  .map(line => line.trim().split(/\s+/).map(x => x.trim()))

const robots = robotsRaw
  .split('\n')
  .map(line => line.trim().split(/\s+/).map(x => x.trim()))

for (let i = 0; i < robots.length; i++) {
  for (let j = 0; j < robots[i].length; j++) {
    robots[i][j] = [robots[i][j], COLORS_MAP[colors[i][j]]]
  }
}

for (let i = robots.length - 1; i >= 0; i--) {
  for (let j = 0; j < robots[i].length; j++) {
    const [_, color] = robots[i][j]
    const col = REVERSE_COLOR_MAP[color]
    const layer = SPECIAL_LAYERS[col] ?? robots.length - i
    robots[i][j] = [robots[i][j][0], { color, layer }]
  }
}


fs.writeFileSync('robots.json', JSON.stringify(robots.flat()))

