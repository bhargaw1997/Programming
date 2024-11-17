class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # To store the medians
        medians = []

        # To keep track of the numbers that need to be removed from the heaps
        outgoing_num = {}

        # Max heap
        small_list = []

        # Min heap
        large_list = []

        # Initialize the max heap by multiplying each element by -1
        for i in range(k):
            heappush(small_list, -nums[i])

        # Transfer the top 50% of the numbers from max heap to min heap
        # while restoring the sign of each number
        for i in range(k // 2):
            element = heappop(small_list)
            heappush(large_list, -element)

        # Variable to keep the heaps balanced
        balance = 0

        i = k
        while True:
            # If the window size is odd
            if k % 2 == 1:
                medians.append(float(-small_list[0]))
            else:
                medians.append((-small_list[0] + large_list[0]) * 0.5)

            # Break the loop if all elements have been processed
            if i >= len(nums):
                break

            # Outgoing number
            out_num = nums[i - k]

            # Incoming number
            in_num = nums[i]
            i += 1

            # If the outgoing number is from max heap
            if out_num <= -small_list[0]:
                balance -= 1
            else:
                balance += 1

            # Add/Update the outgoing number in the hash map
            outgoing_num[out_num] = outgoing_num.get(out_num, 0) + 1

            # If the incoming number is less than the top of the max heap, add it in that heap
            # Otherwise, add it in the min heap
            if in_num <= -small_list[0]:
                balance += 1
                heappush(small_list, -in_num)
            else:
                balance -= 1
                heappush(large_list, in_num)

            # Re-balance the heaps
            if balance < 0:
                heappush(small_list, -heappop(large_list))
            elif balance > 0:
                heappush(large_list, -heappop(small_list))

            # Since the heaps have been balanced, we reset the balance variable to 0.
            balance = 0

            # Remove invalid numbers present in the hash map from top of max heap
            while (
                small_list
                and -small_list[0] in outgoing_num
                and outgoing_num[-small_list[0]] > 0
            ):
                outgoing_num[-small_list[0]] -= 1
                heappop(small_list)

            # Remove invalid numbers present in the hash map from top of min heap
            while (
                large_list
                and large_list[0] in outgoing_num
                and outgoing_num[large_list[0]] > 0
            ):
                outgoing_num[large_list[0]] -= 1
                heappop(large_list)

        return medians