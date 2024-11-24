from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize deque and result list
        dq = deque()
        result = []
        
        # Iterate through the array
        for i in range(len(nums)):
            # Remove elements out of the current window from deque front
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements smaller than current element from deque back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current index to deque
            dq.append(i)
            
            # Append the maximum of the current window to the result list
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
