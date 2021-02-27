#there are a lot of nice staff in collection library
from collections import defaultdict
#we are passing what the default is for the dictionary
animals = defaultdict(list)
print(animals)
#referencing the key'dogs' returns an empty list
print(animals["dogs"])
#now if we will look at animals again it will the key 'dogs' inside
print(animals)

#now we can directly access this list and append items to it
animals["dogs"].append("Spot")
print(animals)
#we can even append items to a key that doesn't exist
animals["cats"].append("Mittens")
print(animals)

#we can continue to access the list with the key dogs
animals["dogs"].append("Fido")
print(animals["dogs"])

#we can initialize our default list with anything, but the list is the most common anything
