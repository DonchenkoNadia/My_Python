def square(x):
    return x*x
lst = [1, 2, -5, 4]
print(lst)

result = list(map(square, lst))
print(result)

anouther_result = []

for i in lst:
    anouther_result.append(square(i))

print(anouther_result)

#a very Pythonic way to do the same
one_more_result = [square(j) for j in lst]

print(one_more_result)
