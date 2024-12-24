# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        minColumn = maxColumn = 0

        def BFS(root):
            nonlocal minColumn, maxColumn
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row,node.val))
                    minColumn = min(minColumn, column)
                    maxColumn = max(maxColumn, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        BFS(root)

        ret = []
        for col in range(minColumn, maxColumn + 1):
            ret.append([val for row, val  in sorted(columnTable[col])])
    
        return ret