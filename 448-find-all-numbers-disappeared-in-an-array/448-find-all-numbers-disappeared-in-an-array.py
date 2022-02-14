class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        if nums[0]!=1:
            for i in range(1,nums[0]):
                res.append(i)
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]+1) and nums[i]!=nums[i-1]:
                # print(nums[i]-nums[i-1]-1)
                for j in range(1,nums[i]-nums[i-1]):
                    res.append(nums[i-1]+j)
                    # print(nums[i-1]+j)
        if nums[-1]!=len(nums):
            for i in range(1,len(nums)-nums[-1]+1):
                res.append(nums[-1]+i)
        return res