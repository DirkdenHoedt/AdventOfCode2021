def part2(path):
    x = 0
    y = 0
    aim = 0
    with open(path) as input:
        for l in input:
            if l.startswith("forward "):
                x += int(l[8:])
                y += int(l[8:]) * aim
            elif l.startswith("up "):
                aim -= int(l[3:])
            elif l.startswith("down "):
                aim += int(l[5:])
    return x * y