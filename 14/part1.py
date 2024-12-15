from parse import parse


def get_robots(path: str) -> list[tuple[int, int, int ,int]]:
    robots: list[tuple[int, int, int ,int]] = []

    with open(path) as f:
        for line in f:
            p_x, p_y, v_x, v_y = parse("p={:d},{:d} v={:d},{:d}", line.strip())
            robots.append((p_x, p_y, v_x, v_y))
    return robots



def move_robots(robots: list[tuple[int, int, int ,int]], d: int, max_x: int, max_y: int):
    for i in range(len(robots)):
        x, y, dx, dy = robots[i]

        x = (x + (dx * d)) % max_x
        y =( y + (dy * d)) % max_y

        robots[i] = (x, y, dx, dy)

def count_robots(robots: list[tuple[int, int, int ,int]], max_x: int, max_y: int):
    sum = [0, 0, 0, 0]

    med_x = (max_x // 2)
    med_y = (max_y // 2)


    for r in robots:
        x, y, _, _ = r
        i = 0

        if x == med_x: continue
        if x > med_x:
            i += 1
        
        if y == med_y: continue
        if y > med_y:
            i += 2

        sum[i] += 1
        #print(r, i)
    
    #print(sum)

    return sum[0] * sum[1] * sum[2] * sum[3]


def print_robots(robots, max_x, max_y):
    for y in range(max_y):
        for x in range(max_x):
            count = 0
            for r in robots:
                rx, ry, _, _ = r
                if rx == x and ry == y:
                    count += 1
            if count == 0:
                print('.', end='')
            else:
                print(count, end='')
        print()



def main():
    robots = get_robots("14/input")

    move_robots(robots, 100, 101, 103)

    #print_robots(robots, 101, 103)

    print(count_robots(robots, 101, 103))



if __name__ == "__main__":
    main()