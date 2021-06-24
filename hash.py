def my_hash(s):
    h = 0
    for i, val in enumerate(s):
        h = h + ord(val) + i**29
    return h

print(my_hash("abacf"))
print(my_hash("abaer"))
