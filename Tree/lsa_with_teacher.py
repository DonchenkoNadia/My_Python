class Node():
    def __init__(self, val, parent = None, left = None, right = None, lvl = 0):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.lvl = lvl

def LSA_helper(p1, p2):
    if p1.parent == p2.parent:
        return p1.parent
    else:
        p1 = p1.parent
        p2 = p2.parent

def LSA(p1, p2):
    if p1 == p2:
        return p1.parent
    while p1.parent != None and p2.parent != None:
        if p1.lvl != p2.lvl:
            if p1.lvl < p2.lvl:
                p2 = p2.parent
            else:
                p1 = p1.parent
        if p1.lvl == p2.lvl:
            LSA_helper(p1, p2)

root = Node(1, None, Node(2, None, Node(3, None, None, None, 2), None, 1), None, 0)

save_root = root

child_left = root.left
child_left.parent = save_root

next_child_left = child_left.left
next_child_left.parent = child_left

ans = LSA(child_left, next_child_left)
print(ans)
