INPUT = open("Day07.txt", 'r')
bags = {}
for line in INPUT:
    s = line.split(" bags contain ")
    color = s[0]
    contents = s[1].split(",")
    cont = []
    for content in contents:
        d = content.strip().split(" ")
        try:
            count = int(d[0])
            name = " ".join(d[1:-1])
        except:
            count = 0
            name = " ".join(d[:-1])
        cont.append((name, count))
    bags[color] = cont
goal = "shiny gold"
dead = "no other"

def has_gold(color):
    if color == goal:
        return True
    if color == dead:
        return False
    return any(has_gold(i) for i, j in bags[color])

print("part 1:", sum(has_gold(i) for i in bags) - 1)

def count(color):
    return sum(j * (count(i) + 1) for i, j in bags[color]) if color != dead else 0

print("part 2:", count(goal))