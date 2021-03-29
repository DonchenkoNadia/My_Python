# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num

"""
#Or my stupied Solution
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i, val in enumerate(lst):
            lst[i] = str(val)
        return int("".join(lst), 2)
"""        
