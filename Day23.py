INPUT = open("Day23.txt", "r").read()
cups = list(map(int, list(INPUT)))

class Cup():
    def __init__(self, number):
        self.id = number
        self.before = self
        self.after = self

    def insert_after(self, c):
        self.after.before = c
        c.after = self.after
        self.after = c
        c.before = self

    def pop(self):
        self.after.before = self.before
        self.before.after = self.after
        self.after = None
        self.before = None
        return self

    def __str__(self):
        return str(self.id)

class Cups():
    def __init__(self, cups):
        self.max = max(cups)
        self.current = Cup(cups[0])
        self.indexes = list(range(len(cups)))
        self.indexes[self.current.id - 1] = self.current
        a = cups[1:]
        a.reverse()
        for i in a:
            self.current.insert_after(Cup(i))
            self.indexes[i - 1] = self.current.after

    def shuffle(self):
        three = []
        for i in range(3):
            three.append(self.current.after.pop())
        three.reverse()
        destination = self.current.id - 1
        while True:
            d = self.find(destination)
            if d is not None and d not in three:
                for i in three:
                    d.insert_after(i)
                break
            destination = destination - 1
            if destination < 1:
                destination = self.max
        self.current = self.current.after


    def find(self, cid):
        return self.indexes[cid - 1]

    def __str__(self):
        a = self.current
        start = a.id
        s = ""
        while True:
            s += str(a.id)
            a = a.after
            if a.id == start:
                return s

    def labels(self):
        a = self.find(1).after
        s = ""
        while a.id != 1:
            s += str(a.id)
            a = a.after
        return s

    def product(self):
        a = self.find(1)
        return a.after.id * a.after.after.id

cup_list = Cups(cups)
for i in range(100):
    cup_list.shuffle()
print("part 1:", cup_list.labels())

cup_list = Cups(cups + list(range(10, 1000000 + 1)))
for i in range(10000000):
    cup_list.shuffle()
print("part 2:", cup_list.product())