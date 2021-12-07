def part2(path):
    pos = []
    with open(path) as input:
        pos = [int(x) for x in input.readline().split(',')]
    fuel_cost = []
    for i in range(2000):
        cost = 0
        for p in pos:
            dist = abs(p - i)
            for x in range(dist + 1):
                cost += x
        fuel_cost.append(cost)
    return min(fuel_cost)