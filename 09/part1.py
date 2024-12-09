# get the index of the last piece of data
def get_last_data_idx(map: list[int]):
    for i in range(len(map) -1, 0, -2):
        #print(i)
        if map[i] != 0:
            return i
    return -1

def main():
    sum = 0

    with open("09/input") as f:
        line = f.readline()
        disk_map = [int(x) for x in line]

        pos = 0

        for i in range(0, len(disk_map), 2):
            #we hit data first

            while disk_map[i] > 0:
                sum += pos * (i // 2)
                disk_map[i] -= 1
                pos += 1
            
            #next we hit empty space
            last_i = get_last_data_idx(disk_map)
            if last_i == -1:
                break

            while disk_map[i + 1] > 0:
                sum += pos * (last_i // 2)
                disk_map[last_i] -= 1

                if disk_map[last_i] == 0:
                    last_i = get_last_data_idx(disk_map)
                    if last_i == -1:
                        break

                disk_map[i + 1] -= 1
                pos += 1
    print(sum)



if __name__ == "__main__":
    main()