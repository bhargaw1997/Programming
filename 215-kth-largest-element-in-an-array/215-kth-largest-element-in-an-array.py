class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=len(nums)
        while k>0:
            i-=1
            k-=1
        return nums[i]
            