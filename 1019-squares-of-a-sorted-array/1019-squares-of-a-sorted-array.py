class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                squar = nums[right]
                right -= 1
            else:
                squar = nums[left]
                left += 1
            result[i] = squar * squar
        return result