

def get_map_and_instructions(path: str):
    map = []
    inst = []

    with open(path) as f:
        line = f.readline()

        while line.strip() != '':
            line = line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
            map.append(line.strip())
            line = f.readline()
        
        while line:
            line = f.readline()
            inst += [char for char in line.strip()]

    boxes = set()
    walls = set()
    robot = []

    for y in range(len(map)):
        for x in range(len(map[0])):
            #print(x)
            char = map[y][x]
            if char == '@': robot = [x, y]
            if char == '[': boxes.add((x, y))
            if char == '#': walls.add((x, y))


    return (walls, boxes, robot, inst)



def print_map(walls, boxes, robot):
    max_x, max_y = (0, 0)

    for x, y in walls:
        if x > max_x: max_x = x
        if y > max_y: max_y = y
    
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            pos = (x, y)
            i = 0
            if pos in boxes:
                i += 1
            if pos in walls:
                i += 2
            if [pos[0], pos[1]] == robot:
                i += 4
            if (x - 1, y) in boxes:
                i += 8
            if i == 0: print('.', end='')
            elif i == 1: print('[', end='')
            elif i == 2: print('#', end='')
            elif i == 4: print('@', end='')
            elif i == 8: print(']', end='')
            else: 
                print(hex(i).removeprefix('0x'), end='')
                quit()
        print()



def score_boxes(boxes):
    sum = 0
    for x, y in boxes:
        sum += (y * 100) + x
    return sum


def get_boxes_or_wall(positions, boxes, walls):
    overlapping = []

    for pos in positions:
        if pos in boxes:
            overlapping.append(pos)
            continue
        if (pos[0] -1, pos[1]) in boxes:
            overlapping.append((pos[0] -1, pos[1]))
            continue
        if pos in walls:
            return False

    return list(set(overlapping))



def main():
    walls, boxes, robot_pos, instructions = get_map_and_instructions("15/input")
    
    directions = {
        '^': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
        'v': (0, 1)
    }

    for i_char in instructions:
        pushing = []
        dir = directions[i_char]

        next_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])

        if next_pos not in walls:
            next_positions = [next_pos]
        else:
            next_positions = False


        while next_positions != False:
            next_positions = get_boxes_or_wall(next_positions, boxes, walls)

            #we hit a wall. break
            if next_positions == False: 
                #print('wall')
                break
            
            #nothing in front of us. Move everything
            if next_positions == []:
                robot_pos[0] += dir[0]
                robot_pos[1] += dir[1]

                for i in range(len(pushing)):
                    pushing[i] = (pushing[i][0] + dir[0], pushing[i][1] + dir[1])
                break

            if dir[1] == 0:
                boxes.remove(next_positions[0])
                pushing.append(next_positions[0])
                if dir[0] == -1:
                    next_positions[0] = (next_positions[0][0] -1, next_positions[0][1])
                else:
                    next_positions[0] = (next_positions[0][0] + 2, next_positions[0][1])
                continue

            next = []

            for box in next_positions:
                boxes.remove(box)
                pushing.append(box)
                box = (box[0], box[1] + dir[1])
                next += [box, (box[0] + 1, box[1])]

            next_positions = next

            continue
        
        boxes = boxes.union(pushing)


    print(score_boxes(boxes))


if __name__ == "__main__":
    main()