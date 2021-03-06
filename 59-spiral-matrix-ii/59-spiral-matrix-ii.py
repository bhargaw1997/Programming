class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        row, col = 0, 0
        x, y = next(directions)
        for i in range(1, n ** 2 + 1):
            matrix[row][col] = i
            if not (0 <= row + x < n and 0 <= col + y < n and matrix[row + x][col + y] == 0):
                x, y = next(directions)
            row += x
            col += y  
        return matrix