class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(6, Node(7, Node(2, Node(9)), Node(7, Node(1), Node(4))), Node(8, Node(1), Node(3, Node(5))))
levels = []


def bfs(node, level):
    if node == None:
        return

    if len(levels) == level:
        levels.append([])

    levels[level].append(node.val)

    bfs(node.left, level + 1)
    bfs(node.right, level + 1)

def dfs(node, parent, grandparent):
    if not node:
        return

    if parent and grandparent and grandparent.val % 2  == 0:
        ans[0] += node.val
    dfs(node.left, node, parent)
    dfs(node.right, node, parent)

bfs(root, 0)

ans = [0]
dfs(root, None, None)

print(levels)
print(f"ans = {ans}")
