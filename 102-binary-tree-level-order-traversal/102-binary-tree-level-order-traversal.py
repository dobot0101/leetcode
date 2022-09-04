# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        answer = []
        q = deque()
        q.append(root)
        
        while q:
            tmp = []
            q_size = len(q)
            for _ in range(q_size):
                current = q.popleft()
                if current:
                    tmp.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            
            if tmp:
                answer.append(tmp)
                
        return answer
            
            
            
        
        
            
            
        