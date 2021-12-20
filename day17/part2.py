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

def part2(path):
    x_min = x_max = y_min = y_max = 0
    with open(path) as input:
        list_nums = list(map(int, re.findall('-?\d+', input.readline())))
        # print(list_nums)
        x_min = list_nums[0]
        x_max = list_nums[1]
        y_min = list_nums[2]
        y_max = list_nums[3]

    count = 0
    for vy in range(y_min, 500):
        ivy = vy
        for vx in range(x_max + 1):
            x = y = 0
            vy = ivy
            while x < x_max and y > y_min:
                x, y, vx, vy = step(x, y, vx, vy)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    count += 1
                    break
    return count
