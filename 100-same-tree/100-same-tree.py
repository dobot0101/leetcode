# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # recursive
#         def checkSame(f, s):
#             if f == None and s == None:
#                 return True
            
#             if (f != None and s == None) or (f == None and s != None):
#                 return False
            
#             if f.val != s.val:
#                 return False
            
#             return checkSame(f.left, s.left) and checkSame(f.right, s.right)
            
#         return checkSame(p, q)
    
        # bfs
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        
        while q1 and q2:
            v1 = q1.popleft()
            v2 = q2.popleft()
            
            if v1 == None and v2 == None:
                continue
            
            if v1 == None or v2 == None:
                return False
            
            if v1.val != v2.val:
                return False
            
            q1.append(v1.left)
            q1.append(v1.right)
            q2.append(v2.left)
            q2.append(v2.right)
            
        return True
            
            
            
        
