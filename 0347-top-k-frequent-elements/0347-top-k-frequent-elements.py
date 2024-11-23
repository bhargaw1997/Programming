from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        min_heap = []

        for num, freq in freq_map.items():
            heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heappop(min_heap)
        return [num for freq, num in min_heap]