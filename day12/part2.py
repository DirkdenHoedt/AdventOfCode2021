from collections import defaultdict
maze = defaultdict(list)

def gen_paths(visited, current, path):
    global maze
    if current == "end":
        yield path
        return
    for i in maze[current]:
        if (
            i.isupper()
            or visited.get(i, 0) == 0
            or all(v < 2 for k, v in visited.items() if k.islower() and k != "start")
        ):
            if i == "start":
                continue
            yield from gen_paths({**visited, i: visited.get(i, 0) + 1}, i, [*path, i])

def part2(path):
    global maze
    maze = defaultdict(list)
    with open(path) as input:
        for l in input:
            l = l.replace("\n", "").split('-')
            maze[l[0]].append(l[1])
            maze[l[1]].append(l[0])
    return len(list(gen_paths({'start': 2}, 'start', ['start'])))