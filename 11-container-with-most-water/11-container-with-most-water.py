class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            if(height[l]>height[r]):
                area = height[r]*(r-l)
                r-=1
            else:
                area = height[l]*(r-l)
                l+=1
            if maxArea<area:
                maxArea=area
        return maxArea
                
                