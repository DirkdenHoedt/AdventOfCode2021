from collections import defaultdict, Counter

def step_pairs(pairs, rules):
    new_out = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            left_pair = pair[0] + rules[pair]
            right_pair = rules[pair] + pair[1]
            new_out[left_pair] += count
            new_out[right_pair] += count
        else:
            new_out[pair] += count
    return new_out

def part2(path):
    raw = ""
    with open(path) as input:
        raw = input.read()
    chain, rules = raw.split("\n\n")
    rules = dict(line.split(" -> ") for line in rules.splitlines())
    pairs = Counter(a + b for a, b in zip(chain, chain[1:]))
    extras = chain[0], chain[-1]
    for i in range(40):
        pairs = step_pairs(pairs, rules)
    final = defaultdict(int)
    for pair, count in pairs.items():
        final[pair[0]] += count
        final[pair[1]] += count
    final[extras[0]] += 1
    final[extras[1]] += 1
    counted = {k: v // 2 for k, v in final.items()}
    return max(counted.values()) - min(counted.values())