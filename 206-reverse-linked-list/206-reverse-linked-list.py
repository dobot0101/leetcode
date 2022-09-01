# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head != None:
            tmp = head
            head = head.next
            tmp.next = node
            node = tmp
        return node
            
