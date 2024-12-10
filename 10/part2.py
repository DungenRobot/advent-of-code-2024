from part1 import get_map_and_trailheads

def score_trail(t_map: list[str], start: tuple[int, int]) -> int:
    score = 0
    x, y = start

    height = int(t_map[y][x])

    if height == 9: 
        return 1

    for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]: 
        if (y + dy >= len(t_map)) or (y + dy < 0) or (x + dx >= len(t_map[0])) or (x + dx < 0): continue

        next = int(t_map[y + dy][x + dx])
        if next == (height + 1):
            score += score_trail(t_map, (x + dx, y + dy))

    return score


def main():
    
    score = 0

    topo_map, trail_heads = get_map_and_trailheads("10/input")

    for head in trail_heads:
        score += score_trail(topo_map, head)

    print(score)



if __name__ == "__main__":
    main()