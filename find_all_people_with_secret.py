meetings = [[0,2,1],[1,3,1],[4,5,1]]
firstPerson = 1

dict = {}
n = 6
max_time = 0

dict[0] = set()
dict[0].add(0)
dict[0].add(firstPerson)

for meeting in meetings:
    max_time = max(meeting[2], max_time)
    if meeting[2] not in dict:
        dict[meeting[2]] = set()
    dict[meeting[2]].add(meeting[0])
    dict[meeting[2]].add(meeting[1])

print(dict)

knowsSecret = set()
knowsSecret.update(dict.get(0))


for time in range(0, max_time+1):
    print(time)
    print(knowsSecret)
    if knowsSecret.intersection(dict.get(time, {})):
        knowsSecret.update(dict.get(time))
    print(time)
    print(knowsSecret)
    print(" ")

print(knowsSecret)
