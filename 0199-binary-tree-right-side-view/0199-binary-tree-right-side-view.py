# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if level == len(ans):
                ans.append(node.val)

            if node.right:
                queue.append((node.right, level+1))

            if node.left:
                queue.append((node.left, level+1))
        return ans