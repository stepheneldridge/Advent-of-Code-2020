INPUT = open("Day16.txt", "r")
data = INPUT.read().split("\n\n")
rules = {}
for i in data[0].split("\n"):
    d = i.split(": ")
    key = d[0]
    vs = d[1].split(" or ")
    v1 = tuple(map(int, vs[0].split("-")))
    v2 = tuple(map(int, vs[1].split("-")))
    # rules[key] = [v1, v2]
    rules[key] = [range(v1[0], v1[1] + 1), range(v2[0], v2[1] + 1)]

my_ticket = list(map(int, data[1].split(":\n")[1].split(",")))

nearby = []
first = True
for i in data[2].split("\n"):
    if first:
        first = False
        continue
    nearby.append(list(map(int, i.split(","))))

sums = 0
invalids = []
for i in range(len(nearby)):
    for j in nearby[i]:
        valid = False
        for k in rules:
            if j in rules[k][0]:
                valid = True
            elif j in rules[k][1]:
                valid = True
        if not valid:
            sums += j
            if i not in invalids:
                invalids.append(i)
print("part 1:", sums)
fields = {}
for i in rules:
    fields[i] = set()
for i in rules:
    for j in range(len(nearby[0])):
        rule_true = True
        for k in range(len(nearby)):
            if k in invalids:
                continue
            if nearby[k][j] not in rules[i][0] and nearby[k][j] not in rules[i][1]:
                rule_true = False
                break
        if rule_true:
            fields[i].add(j)
solutions = {}
solved = set()
while len(solved) < 20:
    for i in fields:
        if len(fields[i] - solved) == 1:
            s = fields[i].pop()
            solutions[i] = s
            solved.add(s)
prod = 1
for i in solutions:
    if "departure" in i:
        prod *= my_ticket[solutions[i]]
print("part 2:", prod)
