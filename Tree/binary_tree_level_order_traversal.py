#14.04 Mega exiced to understand
class Node():
    def __init__ (self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def printTree(root):
    if root:
        return (f"({printTree(root.left)}  {root.value}  {printTree(root.right)})")
    else:
        return (" - ")

def full_tree(depth):
    if depth == 0:
        return None
    return Node(depth, full_tree(depth-1), full_tree(depth-1))

def bfs(root):
    levels = []

    if not root:
        return levels

    def helper(node, level):

        if len(levels) == level:
            levels.append([])

        levels[level].append(node.value)
        
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)


        return levels

    helper(root, 0)

    return levels

root = full_tree(3)
print(printTree(root))
result = bfs(root)
ans = []
for i in range(len(result)-1, -1, -1):
    ans.append(result[i])
print(ans)
