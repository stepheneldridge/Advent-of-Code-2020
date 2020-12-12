INPUT = open("Day12.txt", 'r')
start_1 = ["E", 0, 0]
start_2 = [0, 0]
waypoint = [10, 1]
dirs = {"E": (1, 0), "W": (-1, 0), "N": (0, 1), "S": (0, -1)}
turns = ["N", "E", "S", "W"]
dturn = {"R": 1, "L": -1}
for line in INPUT:
    d = line[0]
    v = int(line[1:])
    if d in dturn:
        r = (dturn[d] * v // 90) % 4
        start_1[0] = turns[(turns.index(start_1[0]) + r)% 4]
        if r == 1:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif r == 2:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif r == 3:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif d == "F":
        x, y = dirs[start_1[0]]
        start_1[1] += x * v
        start_1[2] += y * v
        start_2[0] += waypoint[0] * v
        start_2[1] += waypoint[1] * v
    else:
        dx = dirs[d][0] * v
        dy = dirs[d][1] * v
        start_1[1] += dx
        start_1[2] += dy
        waypoint[0] += dx
        waypoint[1] += dy
print("part 1:", abs(start_1[1]) + abs(start_1[2]))
print("part 2:", abs(start_2[0]) + abs(start_2[1]))

