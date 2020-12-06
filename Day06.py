INPUT = open("Day06.txt", 'r')
groups = INPUT.read().split("\n\n")
questions = "qwertyuiopasdfghjklzxcvbnm"

sums = 0
for group in groups:
    for question in questions:
        if question in group:
            sums += 1
print("part 1:", sums)

sums = 0
for group in groups:
    people = group.split("\n")
    for question in questions:
        all_answer = True
        for person in people:
            if question not in person:
                all_answer = False
                break
        if all_answer:
            sums += 1
print("part 2:", sums)