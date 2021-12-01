def part2(path):
    increases = 0
    last_number = 99999999999
    with open(path) as input:
        xs = [int(x) for x in input]
        for i in range(len(xs) - 2):
            x = xs[i] + xs[i + 1] + xs[i + 2]
            if x > last_number:
                increases += 1
            last_number = x
    return increases