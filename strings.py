#strings are arrays
#strings are immutable arrays of characters
#modifying a string is an illusion: a new string is created, replacing the original
name = "Jaspreet"

print(name[1])
#because strings aren't mutable, you can't use the subscript to do assignment
#name[1] = "e" --- this results in a TypeError

#you can't remove parts of the string
#del name[1] --- this results in a TypeError

#if you wish to do this kind of manipulation,
#the most common approach is to convert the string into a list,
#do the manipulation, and then convert it back.

letters = list(name)
print(letters)
#because this is now a list, you can assign using subscripts
letters[1] = "e"
print(letters)
#using the empty string and the .join() method on that,
#we can convert list back into a string
anouther_name = "".join(letters)
print(name)
print(anouther_name)
