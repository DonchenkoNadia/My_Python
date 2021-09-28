n = 3
nodes = [i for i in range(1, n+1)]
paths = []

def permute(nums):
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)

        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)

        nums.append(n)
    return result

paths = permute(nodes)
print(paths)

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def fitBinaryTree(path):
    root = Node(path[0])
    cur = root
    for i in range(1, len(path)):
        if path[i] > cur.val:
            cur.right = Node(path[i])
        elif path[i] < cur.val:
            cur.left = Node(path[i])
        else:
            print(f"Not possible to create BST from {path}")
            return 0
    return 1
ans = 0
for path in paths:
    if fitBinaryTree(path):
        ans += 1
print(ans)
