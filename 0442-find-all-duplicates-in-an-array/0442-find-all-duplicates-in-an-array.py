class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        current = 0 
        ans = []
        while current < len(nums):
            correct = nums[current] - 1
            if nums[correct] != nums[current]:
                nums[correct], nums[current] = nums[current], nums[correct]
            else:
                current += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans
        