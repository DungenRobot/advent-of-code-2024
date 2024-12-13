

def get_prizes(path: str) -> list[tuple[int, int, int, int, int, int]]:

    prizes = []

    with open(path) as f:
        line = f.readline()
        while line:

            A = line.removeprefix("Button A: ").strip()
            B = f.readline().removeprefix("Button B: ").strip()
            P = f.readline().removeprefix("Prize: ").strip()
            f.readline()

            a_x, a_y = A.split(', ')
            b_x, b_y = B.split(', ')
            p_x, p_y = P.split(', ')

            a_x = int(a_x.removeprefix('X+'))
            a_y = int(a_y.removeprefix('Y+'))

            b_x = int(b_x.removeprefix('X+'))
            b_y = int(b_y.removeprefix('Y+'))

            p_x = int(p_x.removeprefix('X='))
            p_y = int(p_y.removeprefix('Y='))

            prizes.append((a_x, a_y, b_x, b_y, p_x, p_y))

            line = f.readline()

    return prizes



def get_minimum_tokens(a_x: int, a_y: int, b_x: int, b_y: int, p_x: int, p_y: int) -> int:

    denom = ((b_x * a_y) - (b_y * a_x))

    if denom == 0: return 0

    a = ((b_x * p_y) - (b_y * p_x)) / denom
    b = (p_x - (a_x * a)) / b_x

    if round(b) != b: return 0
    if round(a) != a: return 0

    return int((3 * a) + b)




def main():

    prizes = get_prizes("13/input")

    sum = 0

    for machine in prizes:
        sum += get_minimum_tokens(*machine)

    print(sum)


if __name__ == "__main__":
    main()