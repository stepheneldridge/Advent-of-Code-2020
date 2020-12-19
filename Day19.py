import re
INPUT = open("Day19.txt", 'r')
data = INPUT.read().split("\n\n")
messages = data[1].split("\n")
rules = {}
for i in data[0].replace("\"", "").split("\n"):
    d = i.split(": ")
    rules[d[0]] = d[1]

def build(start):
    r = rules[start]
    matches = set(re.findall(r'\d+', r))
    while len(matches) > 0:
        for i in matches:
            r = re.sub(r'\b' + i + r'\b', " ( " + rules[i] + " ) ", r)
        matches = set(re.findall(r'\d+', r))
    return r

regex = build("0").replace(" ", "")
print("part 1:", sum(1 for i in messages if re.fullmatch(regex, i)))

rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
regex1 = "(" + build("42").replace(" ", "") + ")"
regex2 = "(" + build("31").replace(" ", "") + ")"

def brute(i):
    c = len(re.findall(regex1, i)) + 1
    for m in range(1, c):
        for n in range(m + 1, c):
            if re.fullmatch(regex1 + "{%d}" % n + regex2 + "{%d}" % m, i):
                return True
    return False

print("part 2:", sum(brute(i) for i in messages))