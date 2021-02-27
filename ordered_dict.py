#ku ku
from collections import OrderedDict
d = OrderedDict(one = 1, two=2, three=3)
print(d)
d['four'] = 4
print(d)
#the order of elements based on the insertion order
d['pi'] = 3.14
print(d)
#similar to the build-in dict method .keys() is avaliable
print(d.keys())
print(list(reversed(d)))
print(list(reversed(d.values())))
#one of the diffrences with the build-in dict is the support of .move_to_end() method

d.move_to_end("four")
print(d)

print(d.popitem())
print(d.popitem())
print(d)

#specifying the parameter False will return first item
print(d.popitem(False))
print(d)
