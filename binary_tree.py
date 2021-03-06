class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root):
    if root:
        return (f"({printTree(root.left)} {root.val} {printTree(root.right)})")
    else:
        return (" - ")

def countNodes(root):
    if root:
        qty_left = countNodes(root.left)
        qty_right = countNodes(root.right)
        return 1 + qty_left + qty_right
    else:
        return 0

def maxDepth(root):
    if root:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    else:
        return 0

def cnt_at_depth(root, depth):
    if root:
        if depth > 0:
            return cnt_at_depth(root.left, depth-1) + cnt_at_depth(root.right, depth-1)
        elif depth == 0:
            return 1
    return 0

def print_nodes_per_level(root):
    height = maxDepth(root)
    for d in range(height + 1):
	    print(f'Depth: {d} count: {cnt_at_depth(root, d)}')

def print_nodes_per_exact_level(root, depth):
    height = maxDepth(root)
    d = depth
    print (f'At depth: {d} count: {cnt_at_depth(root, d)}')

def full_tree(depth):
    if depth == 0:
        return None
    return Node(depth, full_tree(depth-1), full_tree(depth-1))

def sumRootToLeaf(root):
    path_to_leaf = []
    tot_sum = 0

    def my_traverse(node, path):
        #if not leaf node, we are going on with a path
        if node.left:
            my_traverse(node.left, path + str(node.val))
        if node.right:
            my_traverse(node.right, path + str(node.val))

        #leaf node detect
        if not node.left and not node.right:
            path += str(node.val)
            path_to_leaf.append(path)
            #tot_sum += int(path)
        return path_to_leaf

    for i in my_traverse(root, ""):
        tot_sum += int(i)

    return tot_sum



#root = Node(1, Node(2, Node(7, Node(9), None), None), Node(3))
root = full_tree(3)
print(printTree(root))
print("quantity of nodes: ")
print(countNodes(root))
print("Max depth: ")
print(maxDepth(root))
print("Nodes per level: ")
print(print_nodes_per_level(root))
print("Nodes per exact level: ")
print_nodes_per_exact_level(root, 3)

print(f"result of sumRootToLeaf = {sumRootToLeaf(root)}")
