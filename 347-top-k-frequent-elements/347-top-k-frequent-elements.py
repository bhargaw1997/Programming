class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        ans = []
        for i in range(k):
            max_key = max(dic,key=dic.get)
            ans.append(max_key)
            dic[max_key] = 0
        return ans
            