from part1 import score_garden_map
 ####
#    #
#     ####
#         #
 #########


# unhinged side reducing algorithm
# All sides are stored as a series of four ints. Two coordinates within a shape and a direction pointing out
#
# Taking the following shape, the top middle A side as a value of (1, 0, 1, 0)
#
# AAA
# AAA
# AAA
#
# The top side would be represented as 
# (0, 0, 1, 0), (1, 0, 1, 0), (2, 0, 1, 0)
#
# This function reduces this to be a single side by checking for 
# neighboring side positions with the same direction.
#
#
def reduce_sides(sides: set[tuple[int, int, int, int]]):
    reduced: set[tuple[int, int, int, int]] = set()
    visited: set[tuple[int, int, int, int]] = set()

    while sides != set():
        side = sides.pop()
        
        if side in visited: continue

        reduced.add(side) #this is a new unique side that we count

        #this next block of code ensure it's unique be destroying all the same sides surrounding it
        unvisited = [side]
        while unvisited != []:
            next = unvisited.pop()

            visited.add(next)

            # my instincts tell me that this could be cleaner. 
            # my other instincts remind me this is python I'm writing at 3am
            x, y, dir_x, dir_y = next
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new = (x + dx, y+ dy, dir_x, dir_y)
                if new in sides and new not in visited: unvisited.append(new)

    return reduced


def score_shape(g_map: list[str], pos: tuple[int, int]) -> tuple[int, set[tuple[int, int]]]:

    char = g_map[pos[1]][pos[0]]

    upper_x = len(g_map[0])
    upper_y = len(g_map[1])

    visited: set[tuple[int, int]] = set()
    unvisited: set[tuple[int, int]] = {pos}

    sides: set[tuple[int, int, int, int]] = set()

    while unvisited != set():
        pos = unvisited.pop()
        visited.add(pos)

        x, y = pos

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = (x+dx, y+dy)

            if (new_x, new_y) in visited: continue

            out_of_bounds = (new_x < 0) or (new_y < 0) or (new_x >= upper_x) or (new_y >= upper_y)

            if not out_of_bounds and g_map[new_y][new_x] == char:
                unvisited.add((new_x, new_y))
            else:
                sides.add((x, y, dx, dy)) #change here to add to a sides set
            
    area = len(visited)

    sides = reduce_sides(sides)
    return (area * len(sides), visited) #change here at the end to the scoring math



def main():

    garden_map: list[str] = []

    with open("12/input") as f:
        for line in f:
            garden_map.append(line.strip())

    print(score_garden_map(garden_map, score_shape))

if __name__ == "__main__":
    main()