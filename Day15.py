INPUT = open("Day15.txt", "r")
data = list(map(int, INPUT.read().split(",")))
data.reverse()

for i in range(2020 - len(data)):
    last = data[0]
    if last in data[1:]:
        data = [data[1:].index(last) + 1] + data
    else:
        data = [0] + data
print("part 1:", data[0])

INPUT = open("Day15.txt", "r")
data = list(map(int, INPUT.read().split(",")))

last_said = {}
for i in range(len(data) - 1):
    last_said[data[i]] = i

a = data[-2]
b = data[-1]
for i in range(len(data) - 1, 30000000):
    if b in last_said:
        a = b
        b = i - last_said[b]
    else:
        a = b
        b = 0
    last_said[a] = i
print("part 2:", a)