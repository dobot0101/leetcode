# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        count = 0
        while tmp != None:
            tmp = tmp.next
            count += 1
        
        
        mid_idx = count // 2
        for i in range(mid_idx):
            head = head.next
        
        return head
        
            
        