# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        fast = head.next.next
        slow = head.next
        
        while slow != fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return None
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        
        
        
            
        
        