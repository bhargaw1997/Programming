class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return None
        first_pointer=0
        second_pointer=1
        while(second_pointer<len(nums)):
            if nums[first_pointer] == nums[second_pointer]:
                nums.pop(first_pointer)
                continue
            else:
                first_pointer=second_pointer
                second_pointer+=1
        return len(nums)