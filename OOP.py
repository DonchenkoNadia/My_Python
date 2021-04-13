#object-oriented programming
#is a way of thinking about and implementing our code

#We can add documentation to our own classes, methods,
#and functions using docstrings
def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

print(help(to_seconds))
