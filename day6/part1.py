def part1(path):
    with open(path) as input:
        ages = [int(x) for x in input.readline().split(',')]
    for i in range(80):
        newages = []
        for i, a in enumerate(ages):
            if a == 0:
                newages.append(6)
                newages.append(8)
            else:
                newages.append(a - 1)
        ages = newages
    return len(ages)