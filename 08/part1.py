def get_node_list(map: list[str], bounds: tuple[int, int]) -> dict[str, list[tuple[int, int]]]:
    nodes: dict[str, list[tuple[int, int]]] = {}

    for x in range(bounds[0]):
        for y in range(bounds[1]):
            char = map[y][x]
            if char == '.': continue

            char_positions = nodes.get(char, [])
            char_positions.append((x, y))
            nodes[char] = char_positions
    
    return nodes


def get_anti_nodes(node1, node2) -> list[tuple[int, int]]:
    diff = (node1[0] - node2[0], node1[1] - node2[1])

    #we get the two antinodes at positions (node1 + diff) and (node2 - diff)
    #because diff = (node1 - node2), we'll get the outer values
    return[(node1[0] + diff[0], node1[1] + diff[1]), (node2[0] - diff[0], node2[1] - diff[1])]


def node_in_bounds(node: tuple[int, int], bounds: tuple[int, int]):
    if (node[0] >= bounds[0]) or (node[0] < 0) or (node[1] >= bounds[1]) or (node[1] < 0):
        return False
    return True


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

                anti_node1, anti_node2 = get_anti_nodes(node1, node2)

                if node_in_bounds(anti_node1, bounds):
                    anti_nodes.add(anti_node1)
                if node_in_bounds(anti_node2, bounds):
                    anti_nodes.add(anti_node2)
            
    print(len(anti_nodes))



if __name__ == "__main__":
    main()