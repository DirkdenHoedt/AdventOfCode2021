def part1(path):
    lines = []
    code1 = ''
    code2 = ''
    with open(path) as input:
        for l in input:
            lines.append(l[:-1])
        line_width = len(lines[0])
        counts = [0] * line_width
        for l in lines:
            for i, c in enumerate(l):
                if c == '1':
                    counts[i] += 1
        for c in counts:
            if c > (len(lines) / 2):
                code1 += '1'
                code2 += '0'
            else:
                code1 += '0'
                code2 += '1'
        code1 = int(code1, 2)
        code2 = int(code2, 2)
    return code2 * code1