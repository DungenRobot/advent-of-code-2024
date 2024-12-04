directions: list[tuple[int, int]] = [
    (1, 0),
    (0, 1),
    (1, 1),
    (1,-1)
]

def str_exists(grid: list[str], x: int, y: int, dx: int, dy: int, string: str) -> bool:
    while string != "":
        if not x in range(len(grid[0])) or not y in range(len(grid)): return False
        if grid[y][x] != string[0]: return False
        x += dx
        y += dy
        string = string[1:]
    return True


def main():
    total = 0
    
    grid: list[str] = []
    with open("04/input") as f:
        for line in f:
            grid.append(line.strip())

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            char = grid[y][x]
            if char != 'X': continue

            for dx, dy in directions:
                if str_exists(grid, x, y, dx, dy, "XMAS"):
                    total += 1
                if str_exists(grid, x, y, -dx, -dy, "XMAS"):
                    total += 1
    print(total)




if __name__ =="__main__":
    main()