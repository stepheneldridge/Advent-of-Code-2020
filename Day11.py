INPUT = open("Day11.txt", 'r')
root_grid = []
width = 0
height = 0
for line in INPUT:
    a = list(line.strip())
    root_grid += a
    width = max(width, len(a))
    height += 1

vect = [(0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1), (1, 1), (1, 0), (1, -1)]

def check(grid, o, v, r=False):
    w = o % width + v[0]
    h = o // width + v[1]
    if w >= width or w < 0 or h >= height or h < 0:
        return "."
    this = grid[h * width + w]
    if this == "." and r:
        return check(grid, h * width + w, v, r)
    else:
        return this

def round(nbs, r=False):
    grid = root_grid.copy()
    while True:
        new_grid = grid.copy()
        for i in range(len(grid)):
            this = grid[i]
            if this == ".":
                continue
            neighbors = 0
            for v in vect:
                if check(grid, i, v, r) == "#":
                    neighbors += 1
            if this == "#" and neighbors >= nbs:
                new_grid[i] = "L"
            elif this == "L" and neighbors == 0:
                new_grid[i] = "#"
        if grid == new_grid:
            return grid.count("#")
        grid = new_grid


print("part 1:", round(4))
print("part 2:", round(5, True))