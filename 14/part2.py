from part1 import get_robots, move_robots, print_robots


def are_most_neighbors(robots, ratio: float) -> bool:
    positions = set([(x, y) for x, y, _, _, in robots])
    #print(positions)
    visited = set()
    unvisited = set([positions.pop()])
    #print(unvisited)

    while unvisited != set():

        next = unvisited.pop()
        visited.add(next)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            #print(next)
            pos = (next[0] + dx, next[1] + dy)

            if pos in positions:
                unvisited.add(pos)
                positions.remove(pos)

    #print(len(visited) / (len(visited) + len(positions)))
    
    return len(visited) / (len(visited) + len(positions)) > ratio


def main():
    robots = get_robots("14/input")

    i = 0

    while not are_most_neighbors(robots, 0.02):
        move_robots(robots, 1, 101, 103)
        #print(i)
        #print_robots(robots, 101, 103)
        i += 1

    print(i)
    print_robots(robots, 101, 103)


if __name__ == "__main__":
    main()