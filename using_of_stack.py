class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Deque():
    def __init__(self):
        self.top_left = None
        self.top_right = None

    def push_left(self, x):
        node = Node(x)

        node.val = x
        node.next = self.top_left
        self.top_left = node

    def push_right(self, x):
        node = Node(x)

        node.val = x
        node.next = self.top_right
        self.top_right = node

    def print(self):
        print("Printing Deque")
        temp1 = self.top_left

        while temp1:
            print(temp1.val)
            temp1 = temp1.next

        temp2 = self.top_right

        while temp2.next != None:
            #print(temp2.val)
            temp2 = temp2.next

        #print("first element of right stack: ")
        #print(temp2.val)

        while temp2:
            print(temp2.val)
            temp2 = temp2.next

q = Deque()
s = "aabbcc"

for i in range(len(s)):
    if i % 2 == 1:
        q.push_left(s[i])
    else:
        q.push_right(s[i])


q.print()
