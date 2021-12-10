def part2(path):
    scores = []
    with open(path) as input:
        for l in input:
            l = l.replace("\n", "")
            stack = []
            corrupt = False
            for c in l:
                if c == '(' or c == '[' or c == '{' or c == '<':
                    stack.append(c)
                if c == ')' or c == ']' or c == '}' or c == '>':
                    d = stack.pop()
                    if c == ')' and d != '(':
                        corrupt = True
                        break
                    if c == ']' and d != '[':
                        corrupt = True
                        break
                    if c == '}' and d != '{':
                        corrupt = True
                        break
                    if c == '>' and d != '<':
                        corrupt = True
                        break
            if not corrupt:
                score = 0
                for i in reversed(stack):
                    score *= 5
                    if i == '(':
                        score += 1
                    if i == '[':
                        score += 2
                    if i == '{':
                        score += 3
                    if i == '<':
                        score += 4
                scores.append(score)
    scores.sort()
    # print(scores)
    return scores[int(len(scores) / 2)]