from collections import deque

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1, Node(2, Node(4, Node(5), Node(6))), Node(3, Node(7), Node(8)))

queue = deque()
