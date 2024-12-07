def target_possible(target_value: int, base: int, remaining: list[int]) -> bool:

    if len(remaining) == 0:
        return target_value == base

    #all operations increase the final value, and no 0s are present. 
    #If both values are above the target, we know the final value isn't possible
    #It turns out this optimization isn't very helpful
    if (base + remaining[0] > target_value) and (base * remaining[0] > target_value):
        return False

    if target_possible(target_value, base + remaining[0], remaining[1:]):
        return True
    else:
        return target_possible(target_value, base * remaining[0], remaining[1:])


def main():
    sum = 0

    with open("07/input") as f:
        for line in f:
            target, vals = line.strip().split(": ")
            target = int(target)
            vals = [int(x) for x in vals.split(' ')]

            if target_possible(target, vals[0], vals[1:]):
                sum += target
    print(sum)


if __name__ == "__main__":
    main()

