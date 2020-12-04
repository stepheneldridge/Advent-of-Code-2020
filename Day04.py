import re
INPUT = open("Day04.txt", 'r')
data = INPUT.read().split("\n\n")
passports = []
for p in data:
    fields = re.split(r'\s', p)
    d = {}
    for i in fields:
        s = i.split(":")
        d[s[0]] = s[1]
    passports.append(d)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
def check(p):
    for j in fields:
        if j not in p:
            return False
    return True

valids = 0
for p in passports:
    valids += check(p)
print("part 1:", valids)

def num(l, h, v):
    try:
        value = int(v)
        return value <= h and value >= l
    except:
        return False

def validate(key, value):
    if key == "byr":
        return num(1920, 2002, value)
    elif key == "iyr":
        return num(2010, 2020, value)
    elif key == "eyr":
        return num(2020, 2030, value)
    elif key == "hgt":
        if value[-2:] == "in":
            return num(59, 76, value[:-2])
        elif value[-2:] == "cm":
            return num(150, 193, value[:-2])
        return False
    elif key == "hcl":
        return re.fullmatch(r'#[a-f0-9]{6}', value) is not None
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return re.fullmatch(r'\d{9}', value) is not None
    return True

valids = 0
for p in passports:
    if check(p):
        valid = True
        for key, value in p.items():
            if not validate(key, value):
                valid = False
                break
        valids += valid
print("part 2:", valids)
