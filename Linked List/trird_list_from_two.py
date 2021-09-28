class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head1 = ListNode(1, ListNode(4))
head2 = ListNode(2, ListNode(5))



newList = ListNode(0)

while head1 and head2:

    if head1.val < head2.val:
        newList.next = head1
        head1 = head1.next
    else:
        newList.next = head2
        head2 = head2.next

def printList(cur):
    while cur:
        print(cur.val)
        cur = cur.next

printList(newList)
