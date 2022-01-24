intervals = [[13,15],[1,13]]

events = []
for interval in intervals:
    events.append([interval[0],1])
    events.append([interval[1],-1])

events.sort()
print(events)

rooms = 0
cnt = 0
for event in events:
    cnt += event[1]
    rooms = max(rooms, cnt)

print(rooms)
