class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0

        while start < len(nums):
            num = nums[start]
            if num < len(nums) and start != num:
                nums[num], nums[start] =nums[start], nums[num]
            else:
                start += 1
            
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)