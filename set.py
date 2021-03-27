#in Math a set is a well-defined collection of distinct objects
#Python's built-in set type has the following characteristics:
# - sets are unordered
# - elements are unique and duplicate elements are not allowed
# - set itself may be modified,
#   but the elements contained in the set must be hashable
#  if you will open Python and type hash() and put your object in there
#  and hit Enter and it does not Error, then it means that your object is hashable

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

set1 = set(arr1)
set2 = set(arr2)
set3 = set(arr3)
print (sorted(list(set2 & set1 & set3)))

#print(fib(4, seen))
#print(seen)
