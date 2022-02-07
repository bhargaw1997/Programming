class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        import sys
        nums.sort()
        res=sys.maxsize
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    return sum
                if abs(target-sum)<res:
                    res=abs(target-sum)
                    finalres=sum
                if sum<target:
                    j+=1
                elif sum>target:
                    k-=1      
        return finalres