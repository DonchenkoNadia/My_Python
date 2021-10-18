'''
DMITRII repetitor, [11.10.21 18:39]
Есть n команд, которые играют матчи вкруговую каждая с каждой.
Пусть раунд — такой набор матчей, которые могут играться одновременно.
Задача — написать функцию, которая на вход принимает n,
а на выходе — последовательность раундов и матчи, играющиеся в рамках каждого из раундов.
Количество раундов должно быть минимальным.

DMITRII repetitor, [11.10.21 18:41]
>> 3
>> [[(1, None), (2, 3)], [(3, None), (1, 2)], [(2, None), (3, 1)]]

>> 4
>> [[(1, 4), (2, 3)], [(3, 4), (1, 2)], [(2, 4), (3, 1)]]

>> 6
>> [[(1, 6), (2, 5), (3, 4)],
[(5, 6), (1, 4), (2, 3)],
[(4, 6), (5, 3), (1, 2)], [(3, 6), (4, 2), (5, 1)], [(2, 6), (3, 1), (4, 5)]]
'''
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
