class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt=0
        for i,v in enumerate(nums):
            if(v==0):
                first_zero_index=i
                zero_cnt+=1
                if(zero_cnt>1):
                    return [0]*len(nums)
        if zero_cnt == 1:
            nums[first_zero_index]=1
            mul = 1
            for i in nums:
                mul *= i
            ans = [0] * len(nums)
            ans[first_zero_index] = mul
            return ans
        mul = 1
        for i in nums:
            mul *= i
        ans=[]
        for i in nums:
            ans.append(mul//i)
        return ans
        
                