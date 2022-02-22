class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        lastsum = maxsum

        for i in range(1,len(nums)):
            lastsum = max(lastsum+nums[i],nums[i])
            maxsum = max(maxsum, lastsum)

        return maxsum