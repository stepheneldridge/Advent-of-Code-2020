INPUT = open("Day13.txt", 'r')
data = INPUT.read().split("\n")
time = int(data[0])
slopes = []
gap = 0
gaps = []
for i in data[1].split(","):
    try:
        slopes.append(int(i))
        gaps.append(gap)
    except:
        pass
    gap += 1
times = []
for i in slopes:
    times.append(-time % i)
delay = min(times)
bus = slopes[times.index(delay)]
print("part 1:", delay*bus)

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    a %= m
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x

prod = 1
for i in slopes:
    prod *= i
# Always use integer division unless you need a float!
print("part 2:", sum(-gaps[i] * modInverse(prod // slopes[i], slopes[i]) * prod // slopes[i] for i in range(len(slopes))) % prod)