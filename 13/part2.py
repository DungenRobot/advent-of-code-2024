from part1 import get_minimum_tokens, get_prizes


def main():

    prizes = get_prizes("13/input")

    sum = 0
    big_num = 10000000000000

    for machine in prizes:
        a_x, a_y, b_x, b_y, p_x, p_y = machine
        machine = (a_x, a_y, b_x, b_y, p_x + big_num, p_y + big_num)

        sum += get_minimum_tokens(*machine)

    print(sum)


if __name__ == "__main__":
    main()