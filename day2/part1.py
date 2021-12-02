def part1(path):
    x = 0
    y = 0
    with open(path) as input:
        for l in input:
            if l.startswith("forward "):
                x += int(l[8:])
            elif l.startswith("up "):
                y -= int(l[3:])
            elif l.startswith("down "):
                y += int(l[5:])
    return x * y