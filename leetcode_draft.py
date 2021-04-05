from collections import deque

left = deque()
s = "(]"

for ch in s:
    if ch == "(" or ch == "{" or ch == "[":
        left.append(ch)
    elif ch == ")" and left:
        if left.pop() == "(":
            continue
        else:
            print("False")
    elif ch == "}" and left:
        if left.pop() == "{":
            continue
        else:
            print("False")
    elif ch == "]" and left:
        if left.pop() == "[":
            continue
        else:
            print("False")
    else:
        print("False")
