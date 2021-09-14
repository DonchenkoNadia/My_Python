class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(10, Node(8,None,Node(9)), Node(12, Node(11), Node(13)))

def helper(node):
    if node:
        return node.val
    else:
        return 0

def CheckValues(root):

    if root:
        if helper(root.left) > helper(root):
            return 0
        if helper(root.right) < helper(root):
            return 0
        CheckValues(root.left)
        CheckValues(root.right)

    return 1

def CountNodesLeft(root):
    if root:
        return 1 + CountNodesLeft(root.left)
    else:
        return 0

def CountNodesRight(root):
    if root:
        return 1 + CountNodesLeft(root.right)
    else:
        return 0


def CheckHeight(root):
    if root:
        qty_left = CountNodesLeft(root)
        print(f"On left side: {qty_left}")

        qty_right = CountNodesRight(root)
        print(f"On right side: {qty_right}")

        if abs(qty_left-qty_right) <= 1:
            print("It is a balanced binary search tree")
        else:
            print("It is just binary tree")
    else:
        return 0
        

if CheckValues(root):
    print("Seems like a binary search tree")
else:
    print("It is not")

CheckHeight(root)
