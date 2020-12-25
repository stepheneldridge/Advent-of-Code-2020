import re
INPUT = open("Day24.txt", "r")
d = re.compile(r"ne|nw|se|sw|e|w")
inst = []
for i in INPUT:
    inst.append(list(re.findall(d, i)))

grid = {}
vec = {"nw": (-1,1), "ne": (0, 1), "se": (1, -1), "sw": (0, -1), "w": (-1, 0), "e": (1, 0)}
center = (0, 0)

def flip(grid, coord):
    if coord in grid:
        grid[coord] = "black" if grid[coord] == "white" else "white"
    else:
        grid[coord] = "black"

def get(grid, coord):
    if coord in grid:
        return grid[coord]
    return "white"

for i in inst:
    x, y = center
    for j in i:
        dx, dy = vec[j]
        x += dx
        y += dy
    flip(grid, (x, y))

count = 0
for i in grid:
    if grid[i] == "black":
        count += 1
print("part 1:", count)

for _ in range(100):
    flips = set()
    extras = set()
    for coord in grid:
        blacks = 0
        this = grid[coord]
        for d in vec:
            dx, dy = vec[d]
            c = (coord[0] + dx, coord[1] + dy)
            if c in grid:
                if get(grid, c) == "black":
                    blacks += 1
            elif this == "black":
                extras.add(c)
        if this == "white":
            if blacks == 2:
                flips.add(coord)
        elif this == "black":
            if blacks > 2 or blacks == 0:
                flips.add(coord)
    for x, y in extras:
        blacks = 0
        for d in vec:
            dx, dy = vec[d]
            if get(grid, (x + dx, y + dy)) == "black":
                blacks += 1
        if blacks == 2:
            flips.add((x, y))
    for i in flips:
        flip(grid, i)
count = 0
for i in grid:
    if grid[i] == "black":
        count += 1
print("part 2:", count)