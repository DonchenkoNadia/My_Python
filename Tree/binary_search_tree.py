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

edges = [[1, 2], [2, 4], [2, 5], [1, 3], [3, 6], [3, 7], [1, 9]]
graph = {}
root = 1
for x, y in edges:
    if x not in graph:
        graph[x] = []
    graph[x].append(y)

    if y not in graph:
        graph[y] = []
    graph[y].append(x)

def CheckIfBinary(graph):
    if len(graph[root]) > 2:
        return 0
    for i in graph.items():
        if len(i) > 3:
            return 0
    return 1

print(graph)

if CheckIfBinary(graph):
    print("Looks like binary tree!")
else:
    print("It is not a binary tree")
