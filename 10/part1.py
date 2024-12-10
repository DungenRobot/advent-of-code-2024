def get_map_and_trailheads(path: str) -> tuple[list[str], set[tuple[int, int]]]:
    topo_map: list[str] = []
    trail_heads: set[tuple[int, int]] = set()

    y = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            topo_map.append(line)

            if '0' in line:
                x = 0
                for char in line:
                    if char == '0':
                        trail_heads.add((x, y))
                    x += 1
            y += 1
    return (topo_map, trail_heads)


def score_trail(t_map: list[str], start: tuple[int, int]) -> set[tuple[int, int]]:
    reachable: set[tuple[int, int]] = set()
    x, y = start

    height = int(t_map[y][x])

    if height == 9: 
        return {start}

    for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]: 
        if (y + dy >= len(t_map)) or (y + dy < 0) or (x + dx >= len(t_map[0])) or (x + dx < 0): continue

        next = int(t_map[y + dy][x + dx])
        if next == (height + 1):
            s = score_trail(t_map, (x + dx, y + dy))
            reachable = reachable.union(s)

    return reachable


def main():
    topo_map, trail_heads = get_map_and_trailheads("10/input")

    score = 0
    for head in trail_heads:
        s = score_trail(topo_map, head)
        score += len(s)
    print(score)



if __name__ == "__main__":
    main()