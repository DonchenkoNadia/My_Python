class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

p = Node(5)
q = Node(1)

root = Node(3, p, q)

p.left = Node(6)

p.right = Node(2, Node(7), Node(4))

q.left = Node(0)
q.right = Node(8)

def bfs(root):
    levels = []

    def helper(node, level):
        if len(levels) == level:
            levels.append([])
        if node:
            levels[level].append(node.val)
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels

print(bfs(root))

def lca(root, p, q):
    parents = {root: None}
    stack = [root]

    while p not in parents or q not in parents:

        node = stack.pop()

        if node.left:
            parents[node.left] = node
            stack.append(node.left)
        if node.right:
            parents[node.right] = node
            stack.append(node.right)

    ancestors = set()

    while q:
        ancestors.add(q)
        q = parents[q]

    while p not in ancestors:
        p = parents[p]

    return p

ans = lca(root, p, q)
print(ans.val)
