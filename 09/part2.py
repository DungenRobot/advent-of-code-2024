
def print_disk_map(d_map: list[tuple[int, int]]):
    for size, id in d_map:
        id = str(id)
        if id == '-1':
            id = '.'
        print(id * size, end='')
    print()


def find_empty_space_idx(d_map: list[tuple[int, int]], size: int) -> int:
    i = 0
    while i < len(d_map):
        if d_map[i][1] != -1: 
            i += 1
            continue
        if d_map[i][0] >= size:
            return i
        i += 1
    return -1


def create_empty_space(d_map: list[tuple[int, int]]):
    i = len(d_map) - 1
    max_id = 100000000

    while i > 0:
        size, id = d_map[i]
        i -= 1

        if id == -1 or id > max_id: continue
        max_id = id

        idx = find_empty_space_idx(d_map, size)

        if idx == -1 or idx > i: continue

        e_size, _ = d_map[idx]
        d_map[idx] = (e_size - size, -1)

        i += 1

        data = d_map[i]
        d_map[i] = (0, -1)

        d_map.insert(i, (size, -1))

        d_map.insert(idx, data)



def main():
    space_map: list[int]

    with open("09/input") as f:
        line = f.readline()
        space_map = [int(x) for x in line]

    disk_map: list[tuple[int, int]] = []


    for idx, size in enumerate(space_map):
        id = -1
        if idx % 2 == 0:
            id = idx // 2
        disk_map.append((size, id))

    create_empty_space(disk_map)

    sum = 0
    pos = 0

    while disk_map != []:
        size, id = disk_map.pop(0)

        if id == -1:
            pos += size
            continue

        for _ in range(size):
            sum += pos * id
            pos += 1
    
    print(sum)










if __name__ == "__main__":
    main()