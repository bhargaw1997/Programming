from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        if not root:
            return ans

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            ans += 1
            for _ in range(size):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    return ans
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return ans