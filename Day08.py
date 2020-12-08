INPUT = open("Day08.txt", 'r')
program = []
for line in INPUT:
    a = line.strip().split(" ")
    program.append((a[0], int(a[1])))

def run():
    ran = set()
    acc = 0
    pointer = 0
    while True:
        if pointer in ran:
            return acc
        i, j = program[pointer]
        if i == "acc":
            acc += j
        elif i == "jmp":
            pointer += j - 1
        elif i == "nop":
            pass
        ran.add(pointer)
        pointer += 1

print("part 1:", run())

corrupt_list = [i for i in range(len(program)) if program[i][0] in "jmpnop"]
def run_2(change):
    ran = set()
    acc = 0
    pointer = 0
    while True:
        if pointer in ran:
            return None
        if pointer >= len(program):
            return acc
        i, j = program[pointer]
        if pointer == change:
            if i == "jmp":
                i = "nop"
            elif i == "nop":
                i = "jmp"
        if i == "acc":
            acc += j
        elif i == "jmp":
            pointer += j - 1
        elif i == "nop":
            pass
        ran.add(pointer)
        pointer += 1

for i in corrupt_list:
    result = run_2(i)
    if result is not None:
        print("part 2:", result)
        break