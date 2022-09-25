"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                queue.append(node.left)
                queue.append(node.right)
                
                if node.next:
                    node.right.next = node.next.left
                
        return root
        
#         while queue:
#             queue_len = len(queue)
#             tmp_arr = []
#             for _ in range(queue_len):
#                 node = queue.popleft()
#                 tmp_arr.append(node)
                
#                 if node.left:
#                     queue.append(node.left)
                    
#                 if node.right:
#                     queue.append(node.right)
        
#             if tmp_arr:
#                 tmp_arr.append(None)
#                 result += tmp_arr
#                 # result += list(map(str, tmp_arr))
#                 print(result)
        
        return result
                
        