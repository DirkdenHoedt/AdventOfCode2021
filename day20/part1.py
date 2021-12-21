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

raw = open('day20/input.txt').read()
# raw = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
# raw = """#.#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#...

# #..#.
# #....
# ##..#
# ..#..
# ..###"""


def parse_raw():
    algorithm, input = raw.split("\n\n")
    input = input.splitlines()
    parsed = defaultdict(bool)
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            parsed[x, y] = char == "#"
    return algorithm, parsed


algorithm, input = parse_raw()


def next_pixel(x, y, input):
    num = (
        input[x + 1, y + 1]
        | (input[x, y + 1] << 1)
        | (input[x - 1, y + 1] << 2)
        | (input[x + 1, y] << 3)
        | (input[x, y] << 4)
        | (input[x - 1, y] << 5)
        | (input[x + 1, y - 1] << 6)
        | (input[x, y - 1] << 7)
        | (input[x - 1, y - 1] << 8)
    )
    return algorithm[num] == "#"


def bounds(image):
    left = min(x - 1 for x, _ in image.keys())
    right = max(x + 1 for x, _ in image.keys())
    top = min(y - 1 for _, y in image.keys())
    bottom = max(y + 1 for _, y in image.keys())
    return left, right, top, bottom


def step_image(image):
    left, right, top, bottom = bounds(image)
    orig_image = image.copy()
    for x in irange(left, right):
        for y in irange(top, bottom):
            image[x, y] = next_pixel(x, y, orig_image)
    if algorithm[0] == "#" and algorithm[-1] == ".":
        curr = image.default_factory()
        image.default_factory = lambda: not curr


def print_image(image):
    left, right, top, bottom = bounds(image)
    for y in irange(top + 1, bottom - 1):
        for x in irange(left + 1, right - 1):
            print("#" if image[(x, y)] else ".", end="")
        print()


def part_one():
    image = input.copy()
    for i in range(2):
        step_image(image)
    return sum(image.values())


def part_two():
    image = input.copy()
    for i in range(50):
        step_image(image)
    return sum(image.values())

print(part_one())
print(part_two())


# def part1(path):
#     algo = []
#     image = []
#     with open(path) as input:
#         algo = [0 if x == '.' else 1 for x in input.readline()]
#         input.readline()
#         first = True
#         i = 2
#         for l in input:
#             l = l.replace('\n','')
#             if first:
#                 image.append([0] * (len(l) + 4))
#                 image.append([0] * (len(l) + 4))
#                 first = False
#             image.append([0,0])
#             for x in l:
#                 image[i].append(0 if x == '.' else 1)
#             image[i] += [0,0]
#             i += 1
#         image.append([0] * len(image[0]))
#         image.append([0] * len(image[0]))
    
#     newimage = []
#     newimage.append([0] * (len(image[0]) + 2))
#     newimage.append([0] * (len(image[0]) + 2))
#     for x in range(1, len(image) - 1):
#         newimage.append([0,0])
#         for y in range(1, len(image[0]) - 1):
#             bin_raw = ''
#             for a in range(x - 1, x + 2):
#                 for b in range(y - 1, y + 2):
#                     bin_raw += str(image[a][b])
#             index = int(bin_raw, 2)
#             newimage[x + 1].append(algo[index])
#         newimage[x + 1] += [0,0]
#     newimage.append([0] * (len(image[0]) + 2))
#     newimage.append([0] * (len(image[0]) + 2))
    
#     image = newimage
#     newimage = []
#     newimage.append([0] * (len(image[0]) + 2))
#     newimage.append([0] * (len(image[0]) + 2))
#     for x in range(1, len(image) - 1):
#         newimage.append([0,0])
#         for y in range(1, len(image[0]) - 1):
#             bin_raw = ''
#             for a in range(x - 1, x + 2):
#                 for b in range(y - 1, y + 2):
#                     bin_raw += str(image[a][b])
#             index = int(bin_raw, 2)
#             newimage[x + 1].append(algo[index])
#         newimage[x + 1] += [0,0]
#     newimage.append([0] * (len(image[0]) + 2))
#     newimage.append([0] * (len(image[0]) + 2))

#     total = 0
#     for x in newimage:
#         for y in x:
#             if y == 1:
#                 total += 1
#     return total
    
    # print()
    # for x in newimage:
    #     print(''.join(map(str, x)))

