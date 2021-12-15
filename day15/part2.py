import aoc_helper
from aoc_helper import dijkstras, list, map, range

def part2(path):
    risk_map = []
    with open(path) as input:
        risk_map = list(map(int, line.replace('\n', '')).collect() for line in input)
    
    new_data = list(
        row
        + row.mapped(lambda x: x % 9 + 1)
        + row.mapped(lambda x: (x + 1) % 9 + 1)
        + row.mapped(lambda x: (x + 2) % 9 + 1)
        + row.mapped(lambda x: (x + 3) % 9 + 1)
        for row in risk_map
    )
    new_data = (
        new_data
        + new_data.mapped(lambda row: row.mapped(lambda x: x % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 1) % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 2) % 9 + 1))
        + new_data.mapped(lambda row: row.mapped(lambda x: (x + 3) % 9 + 1))
    )

    return dijkstras(new_data)