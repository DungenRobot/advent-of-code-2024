from part1 import get_node_list, node_in_bounds

def get_anti_nodes(node1, node2, bounds) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = [node1, node2]

    diff = (node1[0] - node2[0], node1[1] - node2[1])

    node_pos = (node1[0] + diff[0], node1[1] + diff[1])

    i = 1

    #get all nodes that are at an increasing diff

    while node_in_bounds(node_pos, bounds):
        out.append(node_pos)
        i += 1
        node_pos = (node1[0] + (diff[0] * i), node1[1] + (diff[1] * i))
    
    node_pos = (node2[0] - diff[0], node2[1] - diff[1])

    i = 1

    #get all nodes that are at a decreasing diff

    while node_in_bounds(node_pos, bounds):
        out.append(node_pos)
        i += 1
        node_pos = (node2[0] - (diff[0] * i), node2[1] - (diff[1] * i))

    return out


def main():
    map: list[str] = []

    with open("08/input") as f:
        for line in f:
            map.append(line.strip())
    
    bounds: tuple[int] = (len(map[0]), len(map))

    nodes: dict[str, list[tuple[int, int]]] = get_node_list(map, bounds)

    anti_nodes: set[tuple[int, int]] = set()

    for _, node_positions in nodes.items():
        for i in range(len(node_positions)):
            for j in range(i + 1, len(node_positions)):

                node1 = node_positions[i]
                node2 = node_positions[j]

                new_anti_nodes = get_anti_nodes(node1, node2, bounds)

                anti_nodes = anti_nodes.union(set(new_anti_nodes))

    print(len(anti_nodes))



if __name__ == "__main__":
    main()