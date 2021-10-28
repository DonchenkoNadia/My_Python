class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, x):

        node = Node(x)

        node.val = x
        node.next = self.top
        self.top = node

    def print(self):
        temp = self.top

        while temp:
            print(temp.val)
            temp = temp.next

    #def print_reverse(self): 
        #to print in reverse order


class Deque():
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push_left(self, x):
        self.q1.push(x)

    def push_right(self, x):
        self.q2.push(x)

    def print_deque(self):
        self.q1.print()
        self.q2.print()


s = "aabbcc"

Q = Deque()

for i in range(len(s)):
    if i % 2  == 1:
        Q.push_left(s[i])
    else:
        Q.push_right(s[i])

Q.print_deque()
