class ListNode():
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

head = ListNode(3, ListNode(1, ListNode(5, ListNode(2))))

def showVal(node):
    return node.val


saveHead = head

while head:
    current = head
    while current.next != None:
        if current.val > showVal(current.next):
            temp = current.val
            current.val = showVal(current.next)
            temp_next = current.next
            temp_next.val = temp
        current = current.next
    head = head.next


while saveHead:
    print(saveHead.val)
    saveHead = saveHead.next
