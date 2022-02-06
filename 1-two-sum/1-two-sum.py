class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dictionary = {}
            answer = []

            for i in range(len(nums)):
                secondNumber = target-nums[i]
                if(secondNumber in dictionary.keys()):
                    secondIndex = nums.index(secondNumber)
                    if(i != secondIndex):
                        return sorted([i, secondIndex])

                dictionary.update({nums[i]: i})