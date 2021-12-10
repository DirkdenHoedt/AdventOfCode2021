def part1(path):
    score = 0
    with open(path) as input:
        for l in input:
            l = l.replace("\n", "")
            stack = []
            for c in l:
                if c == '(' or c == '[' or c == '{' or c == '<':
                    stack.append(c)
                if c == ')' or c == ']' or c == '}' or c == '>':
                    d = stack.pop()
                    if c == ')' and d != '(':
                        score += 3
                        break
                    if c == ']' and d != '[':
                        score += 57
                        break
                    if c == '}' and d != '{':
                        score += 1197
                        break
                    if c == '>' and d != '<':
                        score += 25137
                        break
    return score