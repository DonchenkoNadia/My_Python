# A Linked List Node
class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    # Utility function to add an element `x` to the stack
    def push(self, x):        # insert at the beginning

        # allocate a new node in a heap
        node = Node(x)

        # check if stack (heap) is full. Then inserting an element would
        # lead to stack overflow
        if node is None:
            print("Heap Overflow", end='')
            return

        print("Inserting", x)

        # set data in the allocated node
        node.data = x

        # set the `.next` pointer of the new node to point to the current
        # top node of the list
        node.next = self.top

        # update top pointer
        self.top = node

    # Utility function to check if the stack is empty or not
    def isEmpty(self):
        return self.top is None

    # Utility function to return the top element of the stack
    def peek(self):

        # check for an empty stack
        if not self.isEmpty():
            return self.top.data
        else:
            print("The stack is empty")
            return -1

    # Utility function to pop a top element from the stack
    def pop(self):            # remove at the beginning

        # check for stack underflow
        if self.top is None:
            print("Stack Underflow", end='')
            return

        print("Removing", self.peek())

        # update the top pointer to point to the next node
        self.top = self.top.next


if __name__ == '__main__':

    stack = Stack()
    r = 0

    s = "())((()))"

    for ch in s:
        if ch == "(":
            stack.push(ch)
        elif ch == ")" and not stack.isEmpty():
            stack.pop()
        else:
            r += 1

    if stack.isEmpty() and r == 0:
        print("All is correct")
    else:
        print("Not correct")
