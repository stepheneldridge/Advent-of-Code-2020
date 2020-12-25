INPUT = open("Day25.txt", "r").read().split("\n")

def transform(subj, loop):
    value = 1
    for i in range(loop):
        value *= subj
        value %= 20201227
    return value

def untransform(public):
    value = 1
    subj = 7
    count = 0
    while value != public:
        value *= subj
        value %= 20201227
        count += 1
    return count

print("part 1:", transform(int(INPUT[0]), untransform(int(INPUT[1]))))