import itertools as it

a = "aba"
b = "cdc"

def mySubstrings(s):
    comb = []
    for i in range(1, len(s)+1):
        for substr in it.combinations(s, i):
            comb.append("".join(substr))
    return comb

a_comb = mySubstrings(a)
b_comb = mySubstrings(b)

b_set = set(b_comb)
a_set = set(a_comb)

uncommon = []
for substr in a_comb:
    if substr not in b_set:
        uncommon.append(substr)
for substr in b_comb:
    if substr not in a_set:
        uncommon.append(substr)

print(f"a_comb = {a_comb[::-1]}")
print(f"b_comb = {b_comb[::-1]}")
print(f"uncommon = {uncommon}")

max_len = 0
for each in uncommon:
    if len(each) > max_len:
        max_len = len(each)
print(max_len)
