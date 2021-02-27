#groups multiple dictionaries into a single mapping
#provides search across all dictionaries in the map
from collections import ChainMap

ships = {
        "Santa Maria" : 1460,
        "Beagle" : 1820,
        "Enterprise" : 1960,
        }
space_ships = {
        "Atlas D" : 1960,
        "Enterprise" : 1974,
}
chain = ChainMap(ships, space_ships)
print (chain)
#we access thing inside of the chain the same way I would inside of the dictionary
print (chain["Beagle"])

#if you will try to access the key that doesn't exist, you will get a KeyError

del chain["Beagle"]
print (chain)

#here a chain are a little problematic
#any addition to the chain get to the first dictionary associated with the chain
chain["Ariane"] = 1979
print(chain)

#recommendation is to use chains only for reading and searching
