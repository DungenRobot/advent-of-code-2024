from part1 import iterate_line
from functools import cache

@cache
def find_size(num: int, depth: int) -> int:
    line = iterate_line([num])

    if depth == 1:
        return len(line)

    size = 0

    for i in line:
        size += find_size(i, depth - 1)

    return size


def main():
    line = ''
    with open("11/input") as f:
        line = [int(x) for x in f.readline().strip().split(' ')]

    sum = 0

    for i in line:
        sum += find_size(i, 25)

    print(sum)



if __name__ == "__main__":
    main()