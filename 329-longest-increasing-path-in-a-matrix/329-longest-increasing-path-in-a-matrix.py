class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = [[0]*len(matrix[i]) for i in range(len(matrix))]
        
        def helper(i,j):
            if dp[i][j]:
                return dp[i][j]
            
            cur_max_path_len = 1
            for x,y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if x>=0 and x<len(matrix) and y>=0 and y<len(matrix[x])and matrix[x][y] > matrix[i][j]:
                    cur_max_path_len = max(cur_max_path_len,helper(x,y)+1)
            
            dp[i][j] = cur_max_path_len
            return dp[i][j]
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans = max(ans,helper(i,j))
        return ans