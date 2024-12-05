def is_page_valid(rules: dict[int, list[int]], pages: list[int]) -> bool:
    for i in range(1, len(pages) + 1):
        if is_rule_broken(rules, pages[:i]): 
            return False
    return True

def is_rule_broken(rules: dict[int, list[int]], pages: list[int]) -> bool:
    page = pages[-1]

    for rule in rules.get(page, []):
        if rule in pages:
            return True
    
    return False


def add_rule(rules: dict[int, list[int]], line: str):
    x, y = line.split('|')
    x, y = (int(x), int(y))
    rules[x] = rules.get(x, [])
    rules[x].append(y)

def main():

    sum = 0

    rules: dict[int, list[int]] = {}

    with open("05/input") as f:
        parsing_rules = True

        for line in f:

            if line.strip() == "": 
                parsing_rules = False
                continue

            if parsing_rules:
                add_rule(rules, line)

            else:
                pages = [int(x) for x in line.split(',')]

                if is_page_valid(rules, pages):
                    sum += pages[len(pages) // 2]

    print(sum)


if __name__ == "__main__":
    main()