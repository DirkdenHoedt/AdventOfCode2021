import re

def part2(path):
    loc = []
    for i in range(1000):
        loc.append([])
        for j in range(1000):
            loc[i].append(0)

    with open(path) as input:
        for l in input:
            coords = re.findall(r'\d+', l)
            coords = [int(x) for x in coords]
            if coords[1] == coords[3]:
                if coords[0] > coords[2]:
                    temp = coords[0]
                    coords[0] = coords[2]
                    coords[2] = temp
                for i in range(coords[0], coords[2] + 1):
                    loc[i][coords[1]] += 1
            elif coords[0] == coords[2]:
                if coords[1] > coords[3]:
                    temp = coords[1]
                    coords[1] = coords[3]
                    coords[3] = temp
                for i in range(coords[1], coords[3] + 1):
                    loc[coords[0]][i] += 1
            else:
                if coords[0] > coords[2]:
                    temp = coords[0]
                    coords[0] = coords[2]
                    coords[2] = temp
                    temp = coords[1]
                    coords[1] = coords[3]
                    coords[3] = temp
                for i in range(coords[2] - coords[0] + 1):
                    if (coords[1] > coords[3]):
                        loc[coords[0] + i][coords[1] - i] += 1
                    else:
                        loc[coords[0] + i][coords[1] + i] += 1
    count = 0
    for i in range(1000):
        for j in range(1000):
            if loc[i][j] >= 2:
                count += 1
    # print(loc)
    # print()
    # for i in loc:
    #     print(i)
    return count