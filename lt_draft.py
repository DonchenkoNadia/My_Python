import itertools as it
dict = {}
word = "aaba"
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
for i in dict.values():
    print(i)        
'''
for i in range(0, len(word)+1):
    for k in range(0, i+1):
        print(f"k:i = {k}:{i}")
        print(word[k:i])
'''

#The way to get all substrings of one string

def mySubstrings(s):
    comb = []
    for i in range(1, len(s)+1):
        for substr in it.combinations(s, i):
            comb.append("".join(substr))
    return comb

comb = mySubstrings(word)
print(comb)
