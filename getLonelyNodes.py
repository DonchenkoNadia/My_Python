from collections import deque
class Node():
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__ (self):
         return f"({self.left} --- {self.val} --- {self.right})"

def maxDepth(root):
    if root:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    else:
        return 0
def getLonelyNodes(root):
    ans = deque()

    def dfs(node):
        if node.left and not node.right:
            ans.append(node.left.val)
        if node.right and not node.left:
            ans.append(node.right.val)

        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    dfs(root)
    return ans

root = Node(1, Node(2, None, Node(4)), Node(3))
print (root)
print ("height is", maxDepth(root))
print(getLonelyNodes(root))
