class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
            else:
                i+=1
        return res