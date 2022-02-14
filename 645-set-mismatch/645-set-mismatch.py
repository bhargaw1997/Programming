class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        current_index=0
        while(current_index < len(nums)):
            correct_index=nums[current_index]-1
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]

            else:
                current_index += 1
                
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(nums[i])
                res.append(i+1)
        return res