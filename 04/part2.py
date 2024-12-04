directions = [
    ( 1, 1),
    (-1,-1),
    ( 1, -1),
    (-1, 1),
]


def main():
    total = 0
    
    grid: list[str] = []
    with open("04/input") as f:
        for line in f:
            grid.append(line.strip())

    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            char = grid[y][x]
            if char != 'A': continue

            diagonals = 0
            for dx, dy in directions:
                
                if grid[y+dy][x+dx] == 'M' and grid[y-dy][x-dx] == 'S':
                    diagonals += 1
                
            if diagonals == 2: total += 1

    print(total)



if __name__ =="__main__":
    main()