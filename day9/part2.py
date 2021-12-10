hmap = []
truth = []

def find_basins(i, j):
    # print(hmap[i][j], '', end='')
    c = 0
    if i - 1 >= 0:
        # print(i, j)
        # print(hmap)
        if hmap[i-1][j] >= hmap[i][j] and truth[i-1][j] and hmap[i-1][j] != 9:
            truth[i-1][j] = False
            c += find_basins(i-1, j)
    if j - 1 >= 0:
        if hmap[i][j-1] >= hmap[i][j] and truth[i][j-1] and hmap[i][j-1] != 9:
            truth[i][j-1] = False
            c += find_basins(i, j-1)
    if i + 1 < len(hmap):
        if hmap[i+1][j] >= hmap[i][j] and truth[i+1][j] and hmap[i+1][j] != 9:
            truth[i+1][j] = False
            c += find_basins(i+1, j)
    if j + 1 < len(hmap[i]):
        if hmap[i][j+1] >= hmap[i][j] and truth[i][j+1] and hmap[i][j+1] != 9:
            truth[i][j+1] = False
            c += find_basins(i, j+1)
    return c + 1

def part2(path):
    global hmap, truth
    hmap = []
    truth = []
    i = 0
    total = []
    with open(path) as input:
        for line in input:
            line = line[:-1]
            hmap.append([])
            for l in line:
                hmap[i].append(int(l))
            i += 1

    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            c = 0
            if i - 1 >= 0:
                if hmap[i-1][j] <= hmap[i][j]:
                    c += 1
            if j - 1 >= 0:
                if hmap[i][j-1] <= hmap[i][j]:
                    c += 1
            if i + 1 < len(hmap):
                if hmap[i+1][j] <= hmap[i][j]:
                    c += 1
            if j + 1 < len(hmap[i]):
                if hmap[i][j+1] <= hmap[i][j]:
                    c += 1
            if c == 0:
                z = 0
                for x in hmap:
                    truth.append([])
                    for y in x:
                        truth[z].append(True)
                    z += 1
                total.append(find_basins(i, j))
    total.sort()
    return total[-1] * total[-2] * total[-3]