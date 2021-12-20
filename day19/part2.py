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

def rotate(facing, up, point):
    new_point = list([0, 0, 0])
    match facing:
        case "+x":
            new_point[0] = point[0]
            match up:
                case "+y":
                    new_point[1] = point[1]
                    new_point[2] = point[2]
                case "-y":
                    new_point[1] = -point[1]
                    new_point[2] = -point[2]
                case "+z":
                    new_point[1] = point[2]
                    new_point[2] = -point[1]
                case "-z":
                    new_point[1] = -point[2]
                    new_point[2] = point[1]
        case "-x":
            new_point[0] = -point[0]
            match up:
                case "+y":
                    new_point[1] = point[1]
                    new_point[2] = -point[2]
                case "-y":
                    new_point[1] = -point[1]
                    new_point[2] = point[2]
                case "+z":
                    new_point[1] = point[2]
                    new_point[2] = point[1]
                case "-z":
                    new_point[1] = -point[2]
                    new_point[2] = -point[1]
        case "+y":
            new_point[0] = point[1]
            match up:
                case "+x":
                    new_point[1] = point[0]
                    new_point[2] = -point[2]
                case "-x":
                    new_point[1] = -point[0]
                    new_point[2] = point[2]
                case "+z":
                    new_point[1] = point[2]
                    new_point[2] = point[0]
                case "-z":
                    new_point[1] = -point[2]
                    new_point[2] = -point[0]
        case "-y":
            new_point[0] = -point[1]
            match up:
                case "+x":
                    new_point[1] = point[0]
                    new_point[2] = point[2]
                case "-x":
                    new_point[1] = -point[0]
                    new_point[2] = -point[2]
                case "+z":
                    new_point[1] = point[2]
                    new_point[2] = -point[0]
                case "-z":
                    new_point[1] = -point[2]
                    new_point[2] = point[0]
        case "+z":
            new_point[0] = point[2]
            match up:
                case "+x":
                    new_point[1] = point[0]
                    new_point[2] = point[1]
                case "-x":
                    new_point[1] = -point[0]
                    new_point[2] = -point[1]
                case "+y":
                    new_point[1] = point[1]
                    new_point[2] = -point[0]
                case "-y":
                    new_point[1] = -point[1]
                    new_point[2] = point[0]
        case "-z":
            new_point[0] = -point[2]
            match up:
                case "+x":
                    new_point[1] = point[0]
                    new_point[2] = -point[1]
                case "-x":
                    new_point[1] = -point[0]
                    new_point[2] = point[1]
                case "+y":
                    new_point[1] = point[1]
                    new_point[2] = point[0]
                case "-y":
                    new_point[1] = -point[1]
                    new_point[2] = -point[0]
    return tuple(new_point)
def translate(point, off):
    return point[0] + off[0], point[1] + off[1], point[2] + off[2]
def untranslate(src, dest):
    return src[0] - dest[0], src[1] - dest[1], src[2] - dest[2]


rotations = [
    (sa + da, sb + db)
    for sa in "+-"
    for sb in "+-"
    for da in "xyz"
    for db in "xyz"
    if db != da
]

def common_with_offset(reference, new, offset):
    return len(set(reference) & {translate(beacon, offset) for beacon in new})

def report_partial_match(reference, new):
    for reference_beacon in reference:
        for new_beacon in new:
            offset = untranslate(reference_beacon, new_beacon)
            if common_with_offset(reference, new, offset) >= 12:
                return offset

def report_match(reference, new):
    for facing, up in rotations:
        transformed = {rotate(facing,up,point) for point in new}
        found = report_partial_match(reference, transformed)
        if found:
            return {translate(point, found) for point in transformed}, found

def match_one(reports, fixed_reports, matched):
    for i, report in enumerate(reports):
        for other_report, _ in fixed_reports:
            found = report_match(other_report, report)
            if found:
                beacons, _ = found
                matched |= beacons
                fixed_reports.append(found)
                reports.pop(i)
                return

def match(reports):
    matched, *to_match = reports
    fixed_reports = [(matched, (0,0,0))]
    matched = matched.copy()
    while to_match:
        print('finding match:',len(to_match),'left')
        match_one(to_match,fixed_reports,matched)
    return matched, fixed_reports

def part2(path):
    data = []
    with open(path) as input:
        reports = input.read().split("\n\n")
        data = list(
            set(tuple(extract_ints(line)) for line in report.splitlines()[1:])
            for report in reports
        )
    
    beacons, reports = match(data)
    return max(sum(map(abs,untranslate(scanner_a, scanner_b))) for _, scanner_a in reports for _, scanner_b in reports)