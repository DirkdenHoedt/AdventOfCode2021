def part1(path):
    increases = 0
    last_number = 999999999999
    with open(path) as input:
        for x in input:
            x = int(x)
            if x > last_number:
                increases += 1
            last_number = x
    return increases