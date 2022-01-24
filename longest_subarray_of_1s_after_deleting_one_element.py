from collections import deque

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
queue = deque()

def bfs(node, step):

    queue.append(node)

    while queue:
        print(f"LEVEL {step}")
        temp = queue.popleft()
        print(f"Node - {temp.val}")
        if node.left:
            bfs(node.left, step + 1)
        if node.right:
            bfs(node.right, step + 1)

step = 0
bfs(root, step)
