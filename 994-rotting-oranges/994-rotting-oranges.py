# from collections import deque
class Solution:
    def is_safe(self,row,col,grid):
        return(0<= row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==1)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    rotten.append((row,col,0))
                elif grid[row][col]==1:
                    fresh.add((row,col))
        if rotten==[] and not fresh:
            return 0
        if rotten==[]:
            return -1
        
        valid_row=[-1,0,0,1]
        valid_col=[0,-1,1,0]
        
        while(rotten):
            row,col,time=rotten.pop(0)
            for i in range(len(valid_row)):
                new_row = row+valid_row[i]
                new_col = col+valid_col[i]
                if(self.is_safe(new_row, new_col, grid)):
                    grid[new_row][new_col] = 2
                    rotten.append((new_row, new_col, time+1))
                    fresh.remove((new_row, new_col))
        return -1 if fresh else time