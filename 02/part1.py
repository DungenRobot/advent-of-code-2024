def sign(x: int) -> int:
    if x == 0:
        return 0
    return x // abs(x)



def are_levels_safe(levels: list[int]) -> bool:
    last_dir = sign(levels[1] - levels[0])

    for i in range(len(levels) - 1):
        difference = levels[i+1] - levels[i]
        direction = sign(difference)
        magnitude = abs(difference)

        if magnitude <= 0 or magnitude > 3:
            return False
        
        if direction != last_dir:
            return False
        
        last_dir = direction

    return True



def main():
    with open("input") as f:

        safe_reports = 0

        for line in f:
            levels = line.strip().split(' ')
            levels = [int(x) for x in levels]
            
            if are_levels_safe(levels):
                safe_reports += 1

        print(safe_reports)



if __name__ == "__main__":
    main()