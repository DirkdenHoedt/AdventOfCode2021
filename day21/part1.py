from io import DEFAULT_BUFFER_SIZE


def part1(path):
    pos1 = 0
    pos2 = 0
    with open(path) as input:
        pos1 = int(input.readline()[-2:])
        pos2 = int(input.readline()[-2:])
    score1 = 0
    score2 = 0
    dice = 1
    dcount = 0
    print(pos1, pos2)

    while score1 < 1000 and score2 < 1000:
        place1 = dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1
        place1 += dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1
        place1 += dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1

        pos1 += place1
        if pos1 > 10:
            pos1 %= 10
            if pos1 == 0:
                pos1 = 10
        score1 += pos1
        if score1 >= 1000:
            print(score2, dcount)
            return score2 * dcount

        place2 = dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1
        place2 += dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1
        place2 += dice
        dice += 1
        dcount += 1
        if dice > 100:
            dice = 1

        pos2 += place2
        if pos2 > 10:
            pos2 %= 10
            if pos2 == 0:
                pos2 = 10
        score2 += pos2
        if score2 >= 1000:
            print(score1, dcount)
            return score1 * dcount
    if score2 > 1000:
        print(score1, dcount)
        return score1 * dcount
    else:
        print(score2, dcount)
        return score2 * dcount
        