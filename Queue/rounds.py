from collections import deque
que = deque()
rounds = []
n = 6

if n % 2 == 1:
    teams = [i for i in range(0, n+1)]
else:
    teams = [i for i in range(1, n+1)]

for team in teams:
    que.append(team)

k = len(teams)-1
print(k)
while k > 0:
    round = []

    while que:
        team1 = que.popleft()
        team2 = que.pop()
        round.append([team1, team2])

    rounds.append(round)

    for game in round:
        que.append(game[0])
        que.append(game[1])

    k -= 1

for round in rounds:
    print(round)
