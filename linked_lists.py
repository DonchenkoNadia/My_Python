class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))
        node = node.next
        if node:
            print(sep)

def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = SinglyLinkedListNode(data)
    return head


llist_count = 5
llist = SinglyLinkedList()

for i in range(llist_count):
    llist_item = i + 1
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head

print_singly_linked_list(llist.head, '\n')
