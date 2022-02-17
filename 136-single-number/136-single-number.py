from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set=set(nums)
        total = sum(nums)
        hash_set_total = sum(hash_set)*2
        return hash_set_total-total