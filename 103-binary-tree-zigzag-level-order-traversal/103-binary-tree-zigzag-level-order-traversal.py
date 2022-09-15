# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        
        is_left_to_right = False
        
        while queue:
            is_left_to_right = not is_left_to_right
            queue_len = len(queue)
            tmp_arr = []
            for _ in range(queue_len):
                node = queue.popleft()
                
                if node == None:
                    continue
                    
                tmp_arr.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            
            
            if tmp_arr:
                if not is_left_to_right:
                    tmp_arr.reverse()
                result.append(tmp_arr)
                
        return result
                
            
            
                
            
                
                
            
            
        
                    
                
            
            