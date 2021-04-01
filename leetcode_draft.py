strs = ["dog","racecar","car"]
l = list(zip(*strs))
ans = []
print(l)
for i in l:
    if len(set(i)) == 1:
        ans.append(i[0])
print("".join(ans))
