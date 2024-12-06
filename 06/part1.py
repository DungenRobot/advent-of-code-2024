def next_pos_off_map(map: list[str], pos: list[int], dir: list[int]) -> bool:
    x, y = pos
    x += dir[0]
    y += dir[1]
    return x < 0 or y < 0 or x >= len(map[0]) or y >= len(map)

def get_visited_pos(map, pos):
    directions = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]
    facing = 0

    visited: set[tuple[int, int]] = set()

    while True:
        x, y = pos
        dir = directions[facing]

        visited.add((x, y))

        dx, dy = x + dir[0], y + dir[1]

        if next_pos_off_map(map, pos, dir):
            break

        if map[dy][dx] == '#':
            facing = (facing + 1) % 4
            continue

        pos = [dx, dy]

    return visited


def main():
    pos = [0, 0]
    map: list[str] = []

    with open("06/input") as f:
        for line in f:
            if '^' in line:
                pos[0] = line.find('^')
                pos[1] = len(map)
                line = line.replace('^', '.')
            map.append(line.strip())
    
    visited = get_visited_pos(map, pos)

    print(len(visited))


if __name__ == "__main__":
    main()