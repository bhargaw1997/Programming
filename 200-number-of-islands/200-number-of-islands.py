class Solution:
    def dfs(self,row,col,grid):
        if(row<0 or col<0 or row>len(grid)-1 or col>len(grid[0])-1 or grid[row][col]=="0"):
            return None
        grid[row][col]="0"
        self.dfs(row-1,col,grid)
        self.dfs(row,col-1,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row+1,col,grid)       
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island=0
        # row=len(grid)
        # col=len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]=="1"):
                    island+=1
                    self.dfs(row,col,grid)
        return island
                    