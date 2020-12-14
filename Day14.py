INPUT = open("Day14.txt", 'r')
inst = []
for line in INPUT:
    data = line.strip().split(" = ")
    if data[0] == "mask":
        mask = data[1]
        inst.append(("mask", mask))
    else:
        s = data[0].index("[")
        e = data[0].index("]")
        add = int(data[0][s + 1:e])
        value = int(data[1])
        inst.append(("addr", (add, value)))

def apply_mask(mask, value):
    p = 35
    for i in mask:
        if i == "1":
            value |= 1 << p
        elif i == "0":
            value &= -1 ^ (1 << p)
        p -= 1
    return value

memory = {}
mask = "X" * 36
for i, d in inst:
    if i == "mask":
        mask = d
    elif i == "addr":
        memory[d[0]] = apply_mask(mask, d[1])

s = 0
for i in memory:
    s += memory[i]
print("part 1:", s)

def get_addresses(mask, value, start=35):
    adds = []
    p = start
    for i in range(35 - start, 36):
        m = mask[i]
        if m == "1":
            value |= 1 << p
        elif m == "X":
            adds += get_addresses(mask, value ^ (1 << p), start=p - 1) # Toggle
        p -= 1
    adds.append(value)
    return adds

memory = {}
mask = "X" * 36
for i, d in inst:
    if i == "mask":
        mask = d
    elif i == "addr":
        adds = get_addresses(mask, d[0])
        for j in adds:
            memory[j] = d[1]

s = 0
for i in memory:
    s += memory[i]
print("part 2:", s)