class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while(len(stones)>1):
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1-stone_2)
        return -heapq.heappop(stones) if stones else 0
            

# Time complexity : O(N \, \log \, N)O(NlogN).

    # Converting an array into a Heap takes O(N)O(N) time (it isn't actually sorting; it's putting them into an order that allows us to get the maximums, each in O(\log \, N)O(logN) time).

    # Like before, the main loop iterates up to N - 1N−1 times. This time however, it's doing up to three O(\log \, N)O(logN) operation each time; two removes, and an optional add. Like always, the three is an ignored constant. This means that we're doing N \cdot O(\log \, N) = O(N \, \log \, N)N⋅O(logN)=O(NlogN) operations.

# Space complexity : O(N)O(N) or O(\log \, N)O(logN).

    # In Python, converting a list to a heap is done in-place, requiring O(1)O(1) auxillary space, giving a total space complexity of O(1)O(1). Modifying the input has its pros and cons; it saves space, but it means that other functions can't use the same array.

    # In Java though, it's O(N)O(N) to create the PriorityQueue.

    # We could reduce the space complexity to O(1)O(1) by implementing our own iterative heapfiy, if needed.

        