class Node():
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def addNode(node, val):
    if node != None:
        node.val = val
        node.left = None
        node.right = None
    elif val < node.val:
        node.left = addNode(node.left, val)
    else:
        node.right = addNode(node.right, val)
    return node

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)

def helper(node):
    if node:
        return node.val
    else:
        return 0

root = Node(4, None, Node(5, None, Node(7)))
inOrder(root)
temp = root
addNode(temp, 2)
print(" - ")
print(helper(root.right))
