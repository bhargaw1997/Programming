class Solution:

    def __init__(self, nums: List[int]):
        self.indecies = defaultdict(list)
        for i, num in enumerate(nums):
            self.indecies[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indecies[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)