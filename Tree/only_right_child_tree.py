class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6, None, Node(8, Node(7), Node(9))))

def printVal(node):
    if node:
        return node.val
    else:
        return 0

def dfs(node, vertices):
    if node:
        vertices.append(node.val)
        dfs(node.left, vertices)
        dfs(node.right, vertices)
    return 1

# Function to insert nodes in level order
def insertLevelOrder(vertices, root, i, n):

    # Base case for recursion
    if i < n:
        temp = Node(vertices[i])
        root = temp

        # insert right child
        root.right = insertLevelOrder(vertices, root.right,
                                      i + 1, n)
    return root

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)
vertices = []
dfs(root, vertices)
print(vertices)
vertices.sort()
print(vertices)
n = len(vertices)
root = insertLevelOrder(vertices, root, 0, n)
inOrder(root)
