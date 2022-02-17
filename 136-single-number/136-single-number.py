from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for num in nums:
            if num in d.keys():
                d[num]+=1
            else:
                d[num]=1
        for i in d.keys():
            if d[i]==1:
                return i