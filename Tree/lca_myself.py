class TreeNode():
    def __init__(self, val, left = None, right = None, parent = None, level = 0):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.level = level

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))

def bfs(root):
    levels = []

    if not root:
        return levels

    def helper(parent, node, level):

        if level == len(levels):
            levels.append([])

        levels[level].append(node.val)
        node.parent = parent
        node.level = level

        if node.left:
            helper(node, node.left, level + 1)

        if node.right:
            helper(node, node.right, level + 1)

    helper(None, root, 0)

    return levels

print(bfs(root))
