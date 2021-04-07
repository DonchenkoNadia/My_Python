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

#Example from Google course
#The groups_per_user function receives a dictionary, which contains group names
# with the list of users. Users can belong to multiple groups.
#Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
def groups_per_user(group_dictionary):
    user_groups = {}

    for group in group_dictionary:
        print(group)
        for user in group_dictionary[group]:
            print ("   " + user)
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
