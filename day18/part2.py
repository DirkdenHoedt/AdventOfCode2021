from aoc_helper import map
from ast import literal_eval
from copy import deepcopy
from itertools import permutations

def explode(data, path):
    if 1 in path:
        last_1_idx = max(i for i, v in enumerate(path) if v == 1)
        left = data
        for x in path[:last_1_idx]:
            left = left[x]
        if isinstance(left[0], list):
            left = left[0]
            left_idx = 1
            while isinstance(left[1], list):
                left = left[1]
        else:
            left_idx = 0
    else:
        left = None
    if 0 in path:
        last_0_idx = max(i for i, v in enumerate(path) if v == 0)
        right = data
        for x in path[:last_0_idx]:
            right = right[x]
        if isinstance(right[1], list):
            right = right[1]
            right_idx = 0
            while isinstance(right[0], list):
                right = right[0]
        else:
            right_idx = 1
    else:
        right = None
    parent = data
    for x in path[:-1]:
        parent = parent[x]
    left_num, right_num = parent[path[-1]]
    if left:
        left[left_idx] += left_num
    if right:
        right[right_idx] += right_num
    parent[path[-1]] = 0


def split(num):
    return [num // 2, (num + 1) // 2]


def can_explode(data, depth):
    if isinstance(data, int):
        return depth > 4
    return can_explode(data[0], depth + 1) or can_explode(data[1], depth + 1)


def reduce(data, pair, path, exploding):
    if isinstance(pair, int):
        parent = data
        for i in path[:-1]:
            parent = parent[i]
        if pair >= 10 and not exploding:
            parent[path[-1]] = split(pair)
            return True
        return False
    if len(path) > 3:
        return (
            reduce(data, pair[0], path + [0], exploding)
            or reduce(data, pair[1], path + [1], exploding)
            or explode(data, path)
            or True
        )
    return reduce(data, pair[0], path + [0], exploding) or reduce(
        data, pair[1], path + [1], exploding
    )


def reduce_top(data):
    did_action = True
    while did_action:
        did_action = reduce(data, data, [], can_explode(data, 0))
    return data


def magnitude(pair):
    if isinstance(pair, int):
        return pair
    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

def part2(path):
    data = []
    with open(path) as input:
        data = map(literal_eval, input.readlines()).collect()
    return max(
        magnitude(reduce_top([deepcopy(a), deepcopy(b)]))
        for a, b in permutations(data, 2)
    )