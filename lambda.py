#my first lambda function
squared = lambda x: x**2
print(squared(5))

#it could use few variables
add = lambda x, y: x + y
print(add(4, 5))

mult = lambda x, y, z: x*y*z
print(mult(2,2,2))

#it allows also to set default values
power = lambda x, y=2: x ** y
print(power(5, 3))
print(power(5))

#few examples of lambda function being used in conjunction with methods and functions
#SORT
#has two parameters list.sort (key=None, reverse=False)
#let us look at key as we can use a lambda expression to alter the behavior of .sort()
#the .sort method sorts the list in place using only
#less than (<) ot rgeter than(>) comparisons between items.
#Lambda functions allow key to become moch more versatile
names = ['Alf Zed', 'Mike Mo', 'Steve Aardvark']
names.sort(key = lambda x: x.split()[-1].lower())
print(names)
x = 'Alf Zed Aaron'
print(x.split()) #splits name by using " " as a separator and returns the list
print(x.split()[-1].lower()) #takes the last word (item of list)
#lambda function also allow us to set up .sort() method for non-standart objects.
#For example, objects of the our self-created class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'

alex = Person('Alex', 16)
mabel = Person('Mabel', 15)
eddie = Person('Eddie', 12)
p = [alex, mabel, eddie]
print(p)
p.sort(key=lambda x: x.age)
print(p)
p.sort(key=lambda x: x.name)
print(p)

#FILTER
#filter(function, iterable)
#it construct an iterator from those elements of iterable for which function returns true
#it allows quick creation of iterables of items in another iterable that have passed a test
# example on numbers
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
# example on text
nicknames = ['Diamondbacks', 'Braves', 'Orioles', 'Red Sox', 'Cubs', 'White Sox', 'Reds', 'Indians', 'Rockies']
print(nicknames)
short = list(filter(lambda x: len(x) < 6, nicknames))
print(short)

#MAP
#map(function, iterable)
#map() applies a function to an iterable to create a new iterable
nums = list(range(1, 11))
print(nums)
sq_nums = list(map(lambda x: x**2, nums))
print(sq_nums)
#map also can be used to modify a list of tuples
wc_teams = [('Brazil', 21), ('Germany', 19), ('Italy', 18)]
print(wc_teams)
#let us use map() to apply a lambda expression across the entire
#list of tuples, incrementing the number of times each team has taken part.
new_wc_teams = list(map(lambda team: (team[0],  team[1] + 1), wc_teams))
print(new_wc_teams)

#REDUCE
#applies a function cumulatively to the item of a sequence
from functools import reduce

nums = list(range(1, 6))
print(nums)
total = reduce(lambda x, y: x+y, nums)
print(total)
#this is merely a reconstruction of the sum() function
print(sum(nums))
