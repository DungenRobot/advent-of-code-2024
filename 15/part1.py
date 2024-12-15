

def get_map_and_instructions(path: str):
    map = []
    inst = []

    with open(path) as f:
        line = f.readline()

        while line.strip() != '':
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
            if char == 'O': boxes.add((x, y))
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
            if i == 0: print('.', end='')
            elif i == 1: print('O', end='')
            elif i == 2: print('#', end='')
            elif i == 4: print('@', end='')
            else: print('?', end='')
        print()



def score_boxes(boxes):
    sum = 0
    for x, y in boxes:
        sum += (y * 100) + x
    return sum



def main():
    walls, boxes, robot_pos, instructions = get_map_and_instructions("15/input")

    #print_map(walls, boxes, robot_pos)

    directions = {
        '^': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
        'v': (0, 1)
    }

    for i_char in instructions:
        #print(i_char)
        pushing = []
        dir = directions[i_char]

        next_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])

        #print(robot_pos)
        #print(next_pos, next_pos in walls)

        while next_pos not in walls:
            if next_pos in boxes:
                #print('box')
                pushing.append(next_pos)
                boxes.remove(next_pos)
                next_pos = (next_pos[0] + dir[0], next_pos[1] + dir[1])
                continue
            
            #print('no wall or box')

            robot_pos[0] += dir[0]
            robot_pos[1] += dir[1]

            for i in range(len(pushing)):
                #print(pushing[i])
                pushing[i] = (pushing[i][0] + dir[0], pushing[i][1] + dir[1])
                #print(pushing[i])
            break
        
        boxes = boxes.union(pushing)

        #print_map(walls, boxes, robot_pos)

    #print_map(walls, boxes, robot_pos)

    print(score_boxes(boxes))


if __name__ == "__main__":
    main()