INPUT = open("Day05.txt", 'r')
seats = []
for i in INPUT:
    a = i.strip().replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    seats.append(int(a, 2))
print("part 1:", max(seats))

seats.sort()
for i in range(len(seats)):
    a = seats[i]
    b = seats[i + 1]
    if b - a == 2:
        print("part 2:", a + 1)
        break
