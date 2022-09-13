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
        queue = deque()
        queue.append((p, q))

        while queue:
            n1, n2 = queue.popleft()

            if n1 == None and n2 == None:
                continue

            if n1 == None or n2 == None:
                return False

            if n1.val != n2.val:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True
            
            
            
        
