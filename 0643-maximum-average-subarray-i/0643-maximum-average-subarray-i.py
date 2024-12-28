class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = []
        ssum, start = 0, 0
        for end in range(len(nums)):
            ssum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(ssum / k)  # calculate the average
                ssum -= nums[start]  # subtract the element going out
                start += 1  # slide the window
        return max(average)