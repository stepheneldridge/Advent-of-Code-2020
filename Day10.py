INPUT = open("Day10.txt", 'r')
jolts = [0]
for line in INPUT:
    jolts.append(int(line))
jolts.sort()
jolts.append(max(jolts) + 3)
ones = 0
threes = 0
gaps = []
for i in range(len(jolts) - 1):
    diff = jolts[i + 1] - jolts[i]
    if diff== 1:
        ones += 1
    elif diff == 3:
        gaps.append(i)
        threes += 1
print("part 1:", ones * threes)

def get_value(index, end):
    if index > end:
        return None
    else:
        return jolts[index]

def get_path(index, end):
    if index == end:
        return 1
    total = 0
    current = jolts[index]
    for i in range(1, 4):
        j = get_value(index + i, end)
        if j is None:
            break
        if j - current > 3:
            break
        total += get_path(index + i, end)
    return total

prod = get_path(0, gaps[0])
for i in range(len(gaps) - 1):
    prod *= get_path(gaps[i] + 1, gaps[i + 1])
print("part 2:", prod)

