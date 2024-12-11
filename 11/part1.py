def iterate_line(line: list[int]) -> list[int]:
    new_line = []
    for num in line:
        if num == 0:
            new_line.append(1)
            continue
        s_num = str(num)
        if len(s_num) % 2 == 0:
            new_line += [int(s_num[:len(s_num) // 2]), int(s_num[len(s_num) // 2:])]
            continue
        new_line.append(num * 2024)
    return new_line


def main():
    line = ''
    with open("11/input") as f:
        line = [int(x) for x in f.readline().strip().split(' ')]
    
    for i in range(75):
        line = iterate_line(line)
        print(i)

    print(len(line))


if __name__ == "__main__":
    main()