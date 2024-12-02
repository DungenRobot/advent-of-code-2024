def sign(x: int) -> int:
    if x == 0:
        return 0
    return x // abs(x)



def are_levels_safe(levels: list[int], dampener_active: bool = True) -> bool:
    last_dir = sign(levels[1] - levels[0])

    for i in range(len(levels) - 1):
        difference = levels[i+1] - levels[i]
        direction = sign(difference)
        magnitude = abs(difference)

        if magnitude <= 0 or magnitude > 3:
            if dampener_active:
                return try_all_removals(levels)
            return False
        
        if direction != last_dir:
            if dampener_active:
                return try_all_removals(levels)
            return False
        
        last_dir = direction

    return True

def try_all_removals(levels: list[int]) -> bool:
    for i in range(len(levels)):
        new_levels = levels.copy()
        new_levels.pop(i)

        if are_levels_safe(new_levels, False):
            return True
    return False


def main():
    with open("02/input") as f:

        safe_reports = 0

        for line in f:
            levels = line.strip().split(' ')
            levels = [int(x) for x in levels]
            
            if are_levels_safe(levels):
                safe_reports += 1

        print(safe_reports)



if __name__ == "__main__":
    main()