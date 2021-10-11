class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.top = None

    def push(self, x):

        node = Node(x)

        node.val = x
        node.next = self.top
        self.top = node

    def print(self):
        print("Printing Queue")

        temp = self.top

        while temp:
            print(temp.val)
            temp = temp.next

que = Queue()

que.push(5)
que.push(7)
que.print()
que.push(1)

que.print()
