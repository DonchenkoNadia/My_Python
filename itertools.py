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
