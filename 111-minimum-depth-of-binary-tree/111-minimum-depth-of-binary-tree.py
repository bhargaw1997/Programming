# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        mindp = 0
        stop = False

        while que:
            size = len(que)
            mindp += 1

            for _ in range(size):
                cur = que.popleft()

                if not cur.left and not cur.right:
                    stop = True

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

            if stop:
                break

        return mindp
