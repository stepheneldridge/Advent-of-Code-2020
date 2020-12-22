INPUT = open("Day21.txt", 'r')
recipes = []
for i in INPUT:
    d = i.split(" (")
    recipes.append({"has": set(d[0].split(" ")), "allergy": d[1].strip()[9:-1].split(", ")})
allergens = set()
for i in recipes:
    for j in i["allergy"]:
        allergens.add(j)
possible = {}
used = set()
for i in allergens:
    total = None
    for j in recipes:
        if i in j["allergy"]:
            if total is None:
                total = j["has"]
            else:
                total = total.intersection(j["has"])
    possible[i] = total
    used = used.union(total)

unused = 0
for i in recipes:
    unused += len(i["has"] - used)
print("part 1:", unused)
n = set()
defined = {}
while len(n) < len(possible.keys()):
    for i in possible:
        a = possible[i] - n
        if len(a) == 1:
            defined[i] = a.pop()
            n.add(defined[i])
o = sorted(defined.keys())
st = []
for i in o:
    st.append(defined[i])
print("part 2:", ",".join(st))