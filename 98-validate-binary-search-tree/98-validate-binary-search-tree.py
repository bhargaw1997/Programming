# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, lower=-math.inf, upper=math.inf):
            if not root:
                return True
            if(root.val <= lower or root.val>=upper):
                return False
            return valid(root.right,root.val,upper) and valid(root.left,lower,root.val)
        return valid(root)