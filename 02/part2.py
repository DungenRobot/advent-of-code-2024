from part1 import sign, are_levels_safe

def try_all_removals(levels: list[int]) -> bool:
    for i in range(len(levels)):
        new_levels = levels.copy()
        new_levels.pop(i)

        if are_levels_safe(new_levels):
            return True
    return False


def main():
    with open("02/input") as f:

        safe_reports = 0

        for line in f:
            levels = line.strip().split(' ')
            levels = [int(x) for x in levels]
            
            if are_levels_safe(levels) or try_all_removals(levels):
                safe_reports += 1
            
        print(safe_reports)



if __name__ == "__main__":
    main()