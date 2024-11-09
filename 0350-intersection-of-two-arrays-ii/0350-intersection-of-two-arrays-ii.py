from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        result = []

        for i in nums2:
            if counter1[i] > 0:
                result.append(i)
                counter1[i] -= 1
        return result  