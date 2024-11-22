class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0

        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)

        start, end = 0, len(self.prefix_sum) - 1
        while start < end:
            mid = (start + end) // 2
            if target > self.prefix_sum[mid]:
                start = mid + 1
            else:
                end = mid
        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()