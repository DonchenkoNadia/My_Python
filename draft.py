original = ["a", "b", "c"]
num = 123
cnt_lst = list(str(num))
print(cnt_lst)
j = 0
for i, val in enumerate(cnt_lst):
    j += 1
    original.append(val)

print(original)
h = 2
while h < len(original):

    del original[h]
    h += 1
print(original)
