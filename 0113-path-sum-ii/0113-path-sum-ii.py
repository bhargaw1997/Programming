# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, cursum, temp, ans):
        if root is None:
            return

        temp.append(root.val)
        if root.left is None and root.right is None and cursum == root.val:
            ans.append(list(temp))

        self.dfs(root.left, cursum - root.val, temp, ans)
        self.dfs(root.right, cursum - root.val, temp, ans)
        temp.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        self.dfs(root, targetSum, temp, ans)
        return ans   