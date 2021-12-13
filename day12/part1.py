from collections import defaultdict
maze = defaultdict(list)

def gen_paths(visited, current, path):
    global maze
    if current == 'end':
        yield path
        return
    for i in maze[current]:
        if i.isupper() or not i in visited:
            yield from gen_paths({*visited, i}, i, [*path, i])

def part1(path):
    global maze
    maze = defaultdict(list)
    with open(path) as input:
        for l in input:
            l = l.replace("\n", "").split('-')
            maze[l[0]].append(l[1])
            maze[l[1]].append(l[0])
    return len(list(gen_paths({'start'}, 'start', ['start'])))