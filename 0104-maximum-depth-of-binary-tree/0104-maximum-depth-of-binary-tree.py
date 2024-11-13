from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque()
        queue.append(root)

        if root is None:
            return ans

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                element = queue.popleft()

                if element.left is not None:
                    queue.append(element.left)
                
                if element.right is not None:
                    queue.append(element.right)
            ans += 1
        return ans
