import numpy as np
INPUT = open("Day20.txt", 'r')

class Tile:
    def __init__(self, data):
        self.parse_tile(data)
        self.coord = (None, None)

    def parse_tile(self, tile):
        data = tile.split("\n")
        self.id = int(data[0][5:-1])
        arr = []
        for i in data[1:]:
            arr.append(list(i))
        self.array = np.array(arr, dtype=object)
        self.get_sides()

    def get_sides(self):
        self.sides = ["".join(self.array[0,:]), "".join(self.array[:,-1]), "".join(self.array[-1,:]), "".join(self.array[:,0])]

    def fit(self, coord, grid, nex):
        s = []
        for i in nex:
            a = (i[0] + coord[0], i[1] + coord[1])
            if a in grid:
                s.append(grid[a])
            else:
                s.append(None)
        for a in range(2):
            for b in range(4):
                match = True
                for i in range(4):
                    if s[i] is not None:
                        if s[i].sides[(i + 2) % 4] != self.sides[i]:
                            match = False
                            break
                if match:
                    self.coord = coord
                    return coord
                self.array = np.rot90(self.array)
                self.get_sides()
            self.array = np.flip(self.array, axis=1)
            self.get_sides()
        return None

    def inner_area(self):
        return self.array[1:-1, 1:-1]

tiles = []
for i in INPUT.read().split("\n\n"):
    tiles.append(Tile(i))

left = set(tiles[1:])
# up right down left
next_to = [(0, -1), (1, 0), (0, 1), (-1, 0)]
grid = {}
empty = set()
start = tiles[0]
start.coord = (0, 0)
grid[start.coord] = start
for i in next_to:
    empty.add(i)
while len(left) > 0:
    r = []
    for i in left:
        found = False
        for j in empty:
            coord = i.fit(j, grid, next_to)
            if coord:
                empty.remove(coord)
                grid[coord] = i
                for k in next_to:
                    n = (k[0] + coord[0], k[1] + coord[1])
                    if n not in grid:
                        empty.add(n)
                found = True
                r.append(i)
                break
        if found:
            break
    for i in r:
        left.remove(i)

lx, ly, hx, hy = 1 << 32, 1 << 32, 0, 0
for i in tiles:
    x, y = i.coord
    lx = min(lx, x)
    ly = min(ly, y)
    hx = max(hx, x)
    hy = max(hy, y)
corners = [(lx, ly), (lx, hy), (hx, ly), (hx, hy)]
prod = 1
for i in tiles:
    if i.coord in corners:
        prod *= i.id
print("part 1:", prod)

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

m_arr = []
for i in monster:
    m_arr.append(list(i))
m_arr = np.array(m_arr, dtype=object)
overlap = set()
full_map = None
for j in range(ly, hy + 1):
    temp = grid[(lx, j)].inner_area()
    for i in range(lx + 1, hx + 1):
        temp = np.concatenate((temp, grid[(i, j)].inner_area()), axis=1)
    if full_map is not None:
        full_map = np.concatenate((full_map, temp), axis=0)
    else:
        full_map = temp

for _ in range(2):
    for _ in range(4):
        height = len(m_arr)
        width = len(m_arr[0])
        monster_spots = set()
        for i in range(len(m_arr[0])):
            for j in range(len(m_arr)):
                if m_arr[j][i] == "#":
                    monster_spots.add((i, j))
        for x in range(len(full_map[0]) - width):
            for y in range(len(full_map) - height):
                matches = 0
                for px, py in monster_spots:
                    if full_map[py + y][px + x] == "#":
                        matches += 1
                if matches == len(monster_spots):
                    for px, py in monster_spots:
                        overlap.add((px + x, py + y))
        m_arr = np.rot90(m_arr)
    m_arr = np.flip(m_arr, axis=1)
roughness = 0
for i in range(len(full_map[0])):
    for j in range(len(full_map)):
        if full_map[j][i] == "#" and (i, j) not in overlap:
            roughness += 1
print("part 2:", roughness)

# pretty print
for x, y in overlap:
    full_map[y][x] = chr(0x2588)
full_map = np.flip(full_map, axis=0)
for i in full_map:
    print("".join(i).replace(".", " ").replace("#", "~"))