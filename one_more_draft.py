file = {123: "a", 124: "b", 125: "c", 126: "d", 127: "e", 223: "a", 224: "b", 225: "c", 226: "d", 227: "e"}
t1 = 126
t2 = 225

l = 0
r = len(file)

'''
l = 0;
R = len
x0 > (r+l)/2 -> r = l/2

'''
while l > r:
    x = (r+l)//2
    print(f"l = {l}")
    print(f"r = {r}")
    print("  ")
    if t1 < x:
        r = r//2
    if t1 > x:
        l = r//2
        r = len(file) + l // 2
    if t1 == x:
        print(f"Found on {x}")
