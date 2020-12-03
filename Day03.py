INPUT = open("Day03.txt", 'r')
mapyx = []
for line in INPUT:
    mapyx.append(line.strip())

def count(sx, sy, dx, dy):
    width = len(mapyx[0])
    height = len(mapyx)
    trees = 0
    x, y = sx, sy
    for i in range(height):
        if y >= height:
            break
        spot = mapyx[y][x]
        if spot == "#":
            trees += 1
        x += dx
        y += dy
        x %= width
    return trees

print("part 1:", count(0,0,3,1))

print("part 2:", count(0,0,1,1) * count(0,0,3,1) * count(0,0,5,1) * count(0,0,7,1) * count(0,0,1,2))