# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_len = len(queue)
            tmp_arr = []
            for _ in range(queue_len):
                node = queue.popleft()
                tmp_arr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            if tmp_arr:
                result.append(tmp_arr)
        
        result.reverse()
        
        return result
                