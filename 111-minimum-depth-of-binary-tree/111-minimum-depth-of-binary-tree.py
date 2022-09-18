# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        queue = deque()
        queue.append(root)
        min_depth = 0
        while queue:
            min_depth += 1
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if node.left == None and node.right == None:
                    return min_depth
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            