class Node():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def full_tree(depth):
    if depth == 0:
        return None
    return Node(depth, full_tree(depth-1), full_tree(depth-1))

def print_tree(root):
    if root:
        return (f"{print_tree(root.left)} * {root.val} * {print_tree(root.right)}")
    else:
        return (" --- ")

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

root = full_tree(3)
print(print_tree(root))

print(f"result = {sumRootToLeaf(root)}")
