def checkBingo(c):
    for x in range(5):
        if c[x + 0] == c[x + 1] == c[x + 2] == c[x + 3] == c[x + 4] == True:
            return True
        if c[x + 0] == c[x + 5] == c[x + 10] == c[x + 15] == c[x + 20] == True:
            return True
    return False

def part1(path):
    p_input = []
    with open(path) as input:
        for l in input:
            p_input.append(l)
    drawing = [int(x) for x in p_input[0].split(",")]
    p_input = p_input[2:]
    card = 0
    cards = [[]]
    ticked = [[]]
    for l in p_input:
        if l == "\n":
            card += 1
            cards.append([])
            ticked.append([])
        else:
            # print(l[0:2])
            cards[card].append(int(l[0:2]))
            ticked[card].append(False)
            # print(l[3:5])
            cards[card].append(int(l[3:5]))
            ticked[card].append(False)
            # print(l[6:8])
            cards[card].append(int(l[6:8]))
            ticked[card].append(False)
            # print(l[9:11])
            cards[card].append(int(l[9:11]))
            ticked[card].append(False)
            # print(l[12:15])
            cards[card].append(int(l[12:15]))
            ticked[card].append(False)
    for n in drawing:
        for i, x in enumerate(cards):
            for j, y in enumerate(x):
                if y == n:
                    ticked[i][j] = True
        for i in range(len(cards)):
            if checkBingo(ticked[i]):
                sum_unmarked = 0
                for x in range(25):
                    if not ticked[i][x]:
                        sum_unmarked += cards[i][x]
                return sum_unmarked * n