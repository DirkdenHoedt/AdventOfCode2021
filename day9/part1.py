def part1(path):
    hmap = []
    risk = 0
    with open(path) as input:
        i = 0
        for l in input:
            hmap.append([])
            l = l[:-1]
            for h in l:
                hmap[i].append(int(h))
            i += 1
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            c = 0
            if (i - 1) >= 0:
                if hmap[i-1][j] <= hmap[i][j]:
                    c += 1
            if (j - 1) >= 0:
                if hmap[i][j-1] <= hmap[i][j]:
                    c += 1
            if (i + 1) < len(hmap):
                # print(i, j)
                if hmap[i+1][j] <= hmap[i][j]:
                    c += 1
            if (j + 1) < len(hmap[i]):
                if hmap[i][j+1] <= hmap[i][j]:
                    c += 1
            if c == 0:
                risk += hmap[i][j] + 1
    return risk

