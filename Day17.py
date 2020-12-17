INPUT = open("Day17.txt", "r")
data = INPUT.read().split("\n")

cubes = {}
for i in range(len(data[0])):
    for j in range(len(data)):
        cubes[(i, j, 0)] = data[j][i]

around = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i, j, k) == (1, 1, 1):
                continue
            around.append((i - 1, j - 1, k - 1))

def combine(coord, offset):
    return tuple((coord[i] + offset[i] for i in range(len(coord))))

def get(coord, offset):
    n = combine(coord, offset)
    if n in cubes:
        return cubes[n]
    return "."

def cycle():
    changes = []
    for coord in cubes:
        this = cubes[coord]
        neighbors = 0
        for neighbor in around:
            if get(coord, neighbor) == "#":
                neighbors += 1
        if this == "#":
            if neighbors != 2 and neighbors != 3:
                changes.append((coord, "."))
        elif this == ".":
            if neighbors == 3:
                changes.append((coord, "#"))
    return changes

def expand(cubes):
    for i in list(cubes.keys()):
        if cubes[i] == "#":
            for j in around:
                n = combine(i, j)
                if n not in cubes:
                    cubes[n] = "."

for i in range(6):
    expand(cubes)
    changes = cycle()
    for c, v in changes:
        cubes[c] = v

sums = 0
for i in cubes:

    if cubes[i] == "#":
        sums += 1
print("part 1:", sums)

cubes = {}
for i in range(len(data[0])):
    for j in range(len(data)):
        cubes[(i, j, 0, 0)] = data[j][i]

around = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if (i, j, k, l) == (1, 1, 1, 1):
                    continue
                around.append((i - 1, j - 1, k - 1, l - 1))

for i in range(6):
    expand(cubes)
    changes = cycle()
    for c, v in changes:
        cubes[c] = v

sums = 0
for i in cubes:
    if cubes[i] == "#":
        sums += 1
print("part 2:", sums)