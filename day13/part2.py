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

def part2(path):
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
    
    for f in folds:
        dots = do_fold(dots, f[0], f[1])
    
    for y in range(6):
        for x in range(39):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()

    return None