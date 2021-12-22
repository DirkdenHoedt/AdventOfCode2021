from collections import defaultdict
import aoc_helper
from aoc_helper import (
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)

def part2(path):
    pos1 = 0
    pos2 = 0
    with open(path) as input:
        pos1 = int(input.readline()[-2:])
        pos2 = int(input.readline()[-2:])
    target = 21
    states = {}
    states[pos1, pos2, 0, 0, 0] = 1
    wins = [0, 0]
    while states:
        old_states = states
        states = defaultdict(int)
        for (pos_a, pos_b, score_a, score_b, turn), count in old_states.items():
            if score_a >= target or score_b >= target:
                wins[score_b >= target] += count
                continue
            for i in irange(1, 3):
                for j in irange(1, 3):
                    for k in irange(1, 3):
                        roll = i + j + k
                        if turn == 0:
                            new_pos_a = (pos_a + roll - 1) % 10 + 1
                            states[
                                new_pos_a, pos_b, score_a + new_pos_a, score_b, 1
                            ] += count
                        else:
                            new_pos_b = (pos_b + roll - 1) % 10 + 1
                            states[
                                pos_a, new_pos_b, score_a, score_b + new_pos_b, 0
                            ] += count
    return max(wins)
