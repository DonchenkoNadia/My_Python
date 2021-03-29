import re
s =  "hi(name)"

knowledge =[["a","b"]]

d = {k:v for k, v in knowledge}
lst = s.split("(")
result = lst[0]

for i in range(1, len(lst)):
    question, word = lst[i].split(")")
    result += d.get(question, "?") + word
print (result)
