#https://realpython.com/lessons/built-in-dict/
phonebook = {
        "bob":7387,
        "alice":3719,
        "janet":7052,
        }
print (phonebook)
#method .get allows to receive a value None instead of Error
print (phonebook.get("fred"))
#or set up what to return in case ther is no value for "fred" key
print (phonebook.get("fred", 0))

print (phonebook.keys())
print (phonebook.values())
print (phonebook.items())

for name, ext in phonebook.items():
    print(f"Call {name} at x{ext}")

#comprehensions for creating a dictionary
squares = {x : x*x for x in range (2, 8)}
print (squares)

ranks = [("Picard", "Captain"), ("Riker", "Commander"), ("Worf", "Lieutenant")]
rank_dict = {name:rank for name, rank in ranks}
print (rank_dict)

#python keys must be hashable
#O(1) time complexity for lookup, insert, update, and delete operations
