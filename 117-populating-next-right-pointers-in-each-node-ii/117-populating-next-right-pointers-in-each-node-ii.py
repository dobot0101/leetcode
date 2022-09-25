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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left and node.right:
                node.left.next = node.right
            elif node.left and node.right == None:
                next_node = node.next
                while next_node:
                    if next_node.left:
                        node.left.next = next_node.left
                        break
                    elif next_node.right:
                        node.left.next = next_node.right
                        break
                    next_node = next_node.next
                    
            if node.right:
                next_node = node.next
                while next_node:
                    if next_node.left:
                        node.right.next = next_node.left
                        break
                    elif next_node.right:
                        node.right.next = next_node.right
                        break
                    next_node = next_node.next
                        
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
                
                
        return root
                    
                
                    
            
                    
                
