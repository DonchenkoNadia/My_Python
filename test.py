#https://codeforces.com/problemset/problem/66/B?locale=en
field = [4, 2, 3, 3, 2]
ans = 1
l = 0
r = 1
level = max(field[l], field[r])
max_watered_area = 1

for l in range(1, len(field)):
    cur_watered_area = 1
    for r in range(l+1, len(field)):
        if field[r] > level:
            max_watered_area = max(cur_watered_area, max_watered_area)
        else:
            cur_watered_area += 1
print(max_watered_area)
