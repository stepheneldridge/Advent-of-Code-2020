INPUT = open("Day22.txt", 'r')
p = INPUT.read().split("\n\n")
players = []
for i in p:
    cards = i.split("\n")[1:]
    players.append(list(map(int, cards)))
players2 = players.copy()

while len(players[0]) > 0 and len(players[1]) > 0:
    if players[0] > players[1]:
        players[0] = players[0][1:] + [players[0][0], players[1][0]]
        players[1] = players[1][1:]
    else:
        players[1] = players[1][1:] + [players[1][0], players[0][0]]
        players[0] = players[0][1:]
if len(players[0]) > 0:
    winner = players[0]
else:
    winner = players[1]
sums = 0
for i in range(len(winner), 0, -1):
    sums += i * winner[len(winner) - i]
print("part 1:", sums)

def get_state(p):
    return tuple(p[0] + [-1] + p[1])

def play(state):
    previous = set()
    while len(state[0]) > 0 and len(state[1]) > 0:
        s = get_state(state)
        if s in previous:
            return 1, state
        previous.add(s)
        p1 = state[0][0]
        p2 = state[1][0]
        if p1 <= len(state[0]) - 1 and p2 <= len(state[1]) - 1:
            winner, _ = play([state[0][1:p1 + 1], state[1][1:p2 + 1]])
        else:
            if p1 > p2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            state = [state[0][1:] + [state[0][0], state[1][0]], state[1][1:]]
        else:
            state = [state[0][1:], state[1][1:] + [state[1][0], state[0][0]]]
    if len(state[0]) == 0:
        return 2, state
    elif len(state[1]) == 0:
        return 1, state
p, s = play(players2)
winner = s[p - 1]
sums = 0
for i in range(len(winner), 0, -1):
    sums += i * winner[len(winner) - i]
print("part 2:", sums)
