from collections import defaultdict, Counter

def part1(path):
    seq = []
    lookup = defaultdict(list)
    with open(path) as input:
        seq = [x for x in input.readline().replace('\n', '')]
        input.readline()
        for l in input:
            l = l.replace('\n', '')
            l = l.split(' -> ')
            lookup[l[0]].append(l[0][0])
            lookup[l[0]].append(l[1])
            # lookup[l[0]].append(l[0][1])
        # print(lookup)
    
    for _ in range(10):
        new_seq = []
        for i in range(len(seq) - 1):
            s = seq[i] + seq[i+1]
            if (s in lookup):
                new_seq += lookup[s]
            else:
                new_seq += list(seq[i])
        new_seq.append(seq[-1])
        seq = new_seq
    res = dict(Counter(seq))
    max_c = -1
    min_c = 10000000000
    for r in res:
        if res[r] > max_c:
            max_c = res[r]
        if res[r] < min_c:
            min_c = res[r]
    return max_c - min_c