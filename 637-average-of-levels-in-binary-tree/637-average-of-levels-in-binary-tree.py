# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        if root is None:
            return ans
        queue=deque()
        queue.append(root)
        while(queue):
            size=len(queue)
            current_level=[]
            for _ in range(size):
                current_node=queue.popleft()
                current_level.append(current_node.val)
                
                if(current_node.left):
                    queue.append(current_node.left)
                if(current_node.right):
                    queue.append(current_node.right)
                
            ans.append(sum(current_level)/len(current_level))
        return ans