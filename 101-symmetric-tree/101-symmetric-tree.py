# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append((root.left, root.right))
        while queue:
            left_node, right_node = queue.popleft()
            if left_node == None and right_node == None:
                continue
            if left_node == None or right_node == None:
                return False
            if left_node.val != right_node.val:
                return False
            
            queue.append((left_node.left, right_node.right))            
            queue.append((left_node.right, right_node.left))
        
        return True
            
