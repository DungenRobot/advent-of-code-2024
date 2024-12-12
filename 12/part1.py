def score_shape(g_map: list[str], pos: tuple[int, int]) -> tuple[int, set[tuple[int, int]]]:

    char = g_map[pos[1]][pos[0]]

    upper_x = len(g_map[0])
    upper_y = len(g_map[1])

    perimeter = 0

    visited: set[tuple[int, int]] = set()
    unvisited: set[tuple[int, int]] = {pos}

    while unvisited != set():
        pos = unvisited.pop()
        visited.add(pos)

        x, y = pos

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = (x+dx, y+dy)

            if (new_x, new_y) in visited: continue

            out_of_bounds = (new_x < 0) or (new_y < 0) or (new_x >= upper_x) or (new_y >= upper_y)

            if not out_of_bounds and g_map[new_y][new_x] == char:
                unvisited.add((new_x, new_y)) #this position is part of our shape
            else:
                perimeter += 1 #this pos is outside
    
    area = len(visited)

    return (area * perimeter, visited)

#broke this out into it's own function to repeat less code in part2
def score_garden_map(g_map, scoring_function) -> int:
    sum = 0

    visited: set[tuple[int, int]] = set()

    for x in range(len(g_map[0])):
        for y in range(len(g_map)):
            pos = (x, y)
            if pos in visited: continue

            score, positions = scoring_function(g_map, pos)

            visited = visited.union(positions)

            sum += score
    return sum

def main():

    garden_map: list[str] = []

    with open("12/input") as f:
        for line in f:
            garden_map.append(line.strip())

    print(score_garden_map(garden_map, score_shape))


if __name__ == "__main__":
    main()