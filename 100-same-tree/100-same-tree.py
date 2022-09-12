# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkSame(f, s):
            if f == None and s == None:
                return True
            
            if (f != None and s == None) or (f == None and s != None):
                return False
            
            if f.val != s.val:
                return False
            
            return checkSame(f.left, s.left) and checkSame(f.right, s.right)
            
        return checkSame(p, q)
            
        
