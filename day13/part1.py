def do_fold(dots, axis, coord):
    if axis == 'x':
        dots_new = set()
        for _ in range(len(dots)):
            d = dots.pop()
            if d[0] > coord:
                d_new = (d[0] - (2 * (d[0] - coord)), d[1])
                dots_new.add(d_new)
            else:
                dots_new.add(d)
        dots = dots_new
        return dots
    else:
        dots_new = set()
        for _ in range(len(dots)):
            d = dots.pop()
            if d[1] > coord:
                d_new = (d[0], d[1] - (2 * (d[1] - coord)))
                dots_new.add(d_new)
            else:
                dots_new.add(d)
        dots = dots_new
        return dots

def part1(path):
    dots = set()
    folds = []
    with open(path) as input:
        fold = False
        for l in input:
            if l == '\n':
                fold = True
                continue
            if not fold:
                l = l.replace('\n', '').split(',')
                dots.add((int(l[0]), int(l[1])))
            else:
                l = l.replace('\n', '').split('=')
                folds.append((l[0][-1:], int(l[1])))
    
    dots = do_fold(dots, folds[0][0], folds[0][1])
    return len(dots)