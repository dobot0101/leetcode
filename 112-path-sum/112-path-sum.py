# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                
                if node.left == None and node.right == None:
                    if node.val == targetSum:
                        return True
                else:
                    if node.left:
                        node.left.val = node.left.val + node.val
                        queue.append(node.left)

                    if node.right:
                        node.right.val = node.right.val + node.val
                        queue.append(node.right)    
                    
                
                        
        return False
                
                
                