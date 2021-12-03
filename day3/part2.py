def part2(path):
    lines = []
    code1 = ''
    code2 = ''
    with open(path) as input:
        for l in input:
            lines.append(l[:-1])
        i = 0
        # print()
        # print(lines)
        while len(lines) > 1:
            count = 0
            for l in lines:
                if l[i] == '1':
                    count += 1
            if count >= (len(lines) / 2):
                newlines = []
                for l in lines:
                    if l[i] == '1':
                        newlines.append(l)
                lines = newlines
            else:
                newlines = []
                for l in lines:
                    if l[i] == '0':
                        newlines.append(l)
                lines = newlines
            i += 1
            # print(lines)
        code1 = int(lines[0], 2)
    with open(path) as input:
        for l in input:
            lines.append(l[:-1])
        i = 0
        # print()
        # print(lines)
        while len(lines) > 1:
            count = 0
            for l in lines:
                if l[i] == '1':
                    count += 1
            if count >= (len(lines) / 2):
                newlines = []
                for l in lines:
                    if l[i] == '0':
                        newlines.append(l)
                lines = newlines
            else:
                newlines = []
                for l in lines:
                    if l[i] == '1':
                        newlines.append(l)
                lines = newlines
            i += 1
            # print(lines)
        code2 = int(lines[0], 2)
    return code1 * code2