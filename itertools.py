import itertools as it

ar = ["n", "iq", "ue"]

big_str = "".join(ar)
set_sample = set(big_str)

#let us do that with all possible strings
if len(big_str) == len(set_sample):
    print("All symbols were uniq")
    #now let us check if length is maximum
else:
    print("No.... String contains some dublicate symbols")

#Nice example of grouping by value and it's quantity
tree = [1, 1, 1, 1, 2, 2, 3, 3, 3]
blocks = [(k, len(list(v))) for k, v in it.groupby(tree)]
print(blocks) #schoud print: [(1, 4), (2, 2), (3, 3)]

#Nice example, which is not solving N17 Letter
telephone = { "2" : ["a", "b", "c"],
              "3" : ["d", "e", "f"],
              "4" : ["g", "h", "i"],
              "5" : ["j", "k", "l"],
              "6" : ["m", "n", "o"],
              "7" : ["p", "q", "r", "s"],
              "8" : ["t", "u", "v"],
              "9" : ["w", "x", "y", "z"]
}
digits = "23"
n = len(digits)
combinations_base = ""

for digit in digits:
    combinations_base += "".join(telephone.get(digit))

print(combinations_base)
ans = list(it.combinations(combinations_base, n))
print(ans)

#The way to get all substrings of one string 
a = "aba"

def mySubstrings(s):
    comb = []
    for i in range(1, len(s)+1):
        for substr in it.combinations(s, i):
            comb.append("".join(substr))
    return comb

a_comb = mySubstrings(a)

print(f"a_comb = {a_comb[::-1]}")
