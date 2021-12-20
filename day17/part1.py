from itertools import count
import re

def sign(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx -= sign(vx)
    vy -= 1
    return x, y, vx, vy

def tri(x):
    return x * (x + 1) // 2

def part1(path):
    x_min = x_max = y_min = y_max = 0
    with open(path) as input:
        list_nums = list(map(int, re.findall('-?\d+', input.readline())))
        # print(list_nums)
        x_min = list_nums[0]
        x_max = list_nums[1]
        y_min = list_nums[2]
        y_max = list_nums[3]

    min_steps = next(i for i in range(x_min) if (x := tri(i)) >= x_min)
    best_y = 0
    overshot_count = 0
    for vy in count():
        this_vy = vy
        y = 0
        steps = 0
        local_max = 0
        while y > y_min:
            steps += 1
            y += vy
            vy -= 1
            if y > local_max:
                local_max = y
            if y_min <= y <= y_max:
                if steps >= min_steps:
                    # print("best:", this_vy, best_y, local_max)
                    best_y = max(best_y, local_max)
                break
        else:
            overshot_count += 1
            if overshot_count > 100:
                break
    return best_y
