def part1(path):
    count = 0
    with open(path) as input:
        for l in input:
            output = l.split(' | ')[1]
            output = output.split()
            for o in output:
                if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                    count += 1
    return count