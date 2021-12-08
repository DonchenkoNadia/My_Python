x = set()
x.add((0, 0, 0))
x.add((4, 5, 6))
x.add((7, 8, 9))
x.add((4, 5, 6))

print(x)

t = []
for e, y, z in x:
    t.append([e, y, z])
print(t)
