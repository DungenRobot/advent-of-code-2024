from part1 import is_page_valid, add_rule

def fix_pages(rules: dict[int, list[int]], pages: list[int]) -> list[int]:
    output = [pages.pop()]

    while pages != []:
        new_page = pages.pop()

        new_output = output.copy()

        for i in range(len(output) + 1):
            new_output = output.copy()
            new_output.insert(i, new_page)
            if is_page_valid(rules, new_output):
                break
        
        output = new_output

    return output


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

                if not is_page_valid(rules, pages):
                    pages = fix_pages(rules, pages)
                    sum += pages[len(pages) // 2]

    print(sum)


if __name__ == "__main__":
    main()