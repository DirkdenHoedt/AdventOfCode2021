def part2(path):
    with open(path) as input:
        ages = [int(x) for x in input.readline().split(',')]
    ad = [0] * 9
    for a in ages:
        ad[a] += 1
    for i in range(256):
        temp = ad[0]
        ad[0] = ad[1]
        ad[1] = ad[2]
        ad[2] = ad[3]
        ad[3] = ad[4]
        ad[4] = ad[5]
        ad[5] = ad[6]
        ad[6] = temp + ad[7]
        ad[7] = ad[8]
        ad[8] = temp
    count = 0
    for i in ad:
        count += i
    # print(ad)
    return count