lst = [1, 0, 1]
num = "101"
for i, val in enumerate(lst):
    lst[i] = str(val)
print(int("".join(lst), 2))
"""
while head:
    list.append(head.val)
    head = head.next
print (int("".join(list), 2))
"""
