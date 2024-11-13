from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)
        flag = 1

        while queue:
            current_level = []
            level_size = len(queue)

            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)

                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            if flag == 1:
                result.append(current_level)
                flag=0
            else:
                result.append(current_level[ : :-1])
                flag=1
        return result