import aoc_helper
from aoc_helper import dijkstras, list, map, range

def part1(path):
    risk_map = []
    with open(path) as input:
        risk_map = list(map(int, line.replace('\n', '')).collect() for line in input)

    return dijkstras(risk_map)