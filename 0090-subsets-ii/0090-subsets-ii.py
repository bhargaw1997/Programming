from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input to handle duplicates easily
        result = []  # Initialize the result list to store subsets
        
        def backtrack(start, current_subset):
            result.append(current_subset[:])  # Add a copy of current_subset to the result
            for i in range(start, len(nums)):  # Iterate through the remaining elements
                if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                    continue
                current_subset.append(nums[i])  # Include nums[i] in the current subset
                backtrack(i + 1, current_subset)  # Recur to generate further subsets
                current_subset.pop()  # Remove the last element to backtrack
        
        backtrack(0, [])  # Start backtracking with an empty subset
        return result  # Return the list of all subsets