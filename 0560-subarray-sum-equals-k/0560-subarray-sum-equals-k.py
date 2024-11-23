from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = curr_sum = 0
        h = defaultdict(int)

        for num in nums:
            curr_sum += num

            if curr_sum == k:
                count += 1

            count += h[curr_sum - k]

            h[curr_sum] += 1

        return count