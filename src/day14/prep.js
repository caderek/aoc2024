import fs from 'node:fs'
import path from 'node:path'

const robotsRaw = fs.readFileSync('tree.txt', {encoding: 'utf8'}).trim()
const colorsRaw = fs.readFileSync('tree-hex.txt', {encoding: 'utf8'}).trim()

const COLORS_MAP = {
  '#0000ff': '#0000ff',
  '#0000aa': '#0000aa',
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


const colors = colorsRaw
  .split('\n')
  .map(line => line.trim().split(/\s+/).map(x => x.trim()))

const robots = robotsRaw
  .split('\n')
  .map(line => line.trim().split(/\s+/).map(cell => cell.match(/\d+/g).map(Number)))


for (let i = 0; i < robots.length; i++) {
  for (let j = 0; j < robots[i].length; j++) {
    robots[i][j] = [...robots[i][j], COLORS_MAP[colors[i][j]]]
  }
}

fs.writeFileSync('robots.json', JSON.stringify(robots.flat()))

