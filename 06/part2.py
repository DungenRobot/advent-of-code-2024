from part1 import next_pos_off_map, get_visited_pos

def is_map_loop(map, pos) -> bool:

    directions = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]

    facing = 0

    visited: set[tuple[int, int, int]] = set()

    dir = directions[facing]

    while not next_pos_off_map(map, pos, dir):
        x, y = pos
        dir = directions[facing]

        if (x, y, facing) in visited:
            return True
        
        visited.add((x, y, facing))

        dx, dy = x + dir[0], y + dir[1]

        if map[dy][dx] == '#':
            facing = (facing + 1) % 4
            continue

        pos = [dx, dy]

    return False

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
    visited = visited.difference(set((pos[0], pos[1]))) #remove starting pos

    loops = 0

    for x, y in visited:
        map_copy = map.copy()
        line = list(map_copy[y])
        line[x] = '#'
        map_copy[y] = ''.join(line)

        if is_map_loop(map_copy, pos):
            loops += 1

    print(loops)



if __name__ == "__main__":
    main()