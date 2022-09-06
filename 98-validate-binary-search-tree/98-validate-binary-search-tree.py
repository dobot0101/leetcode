# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min, max):
            if root == None:
                return True
            else:
                val = root.val
                if not(val > min and val < max):
                    return False
                
                return helper(root.left, min, val) and helper(root.right, val, max)
        
        min = -2**31 - 1
        max = 2**31
        
        return helper(root, min, max)
                
            