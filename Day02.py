INPUT = open("Day02.txt", 'r')
passwords = []
rules = []
for i in INPUT:
    d = i.split(":")
    passwords.append(d[1].strip())
    rd = d[0].split(" ")
    rn = rd[0].split("-")
    rules.append([int(rn[0]), int(rn[1]), rd[1]])

def check_valid(rule, password):
    x = password.count(rule[2])
    return x >= rule[0] and x <= rule[1]

valids = 0
for i in range(len(passwords)):
    valids += check_valid(rules[i], passwords[i])

print("part 1:", valids)

def check_valid_2(rule, password):
    return (password[rule[0] - 1] == rule[2]) ^ (password[rule[1] - 1] == rule[2])

valids = 0
for i in range(len(passwords)):
    valids += check_valid_2(rules[i], passwords[i])

print("part 2:", valids)