import heapq
class MedianFinder:
    
    # We need to keep track of both min heaps
    def __init__(self):
        self.nums_high = []
        self.nums_low = []

    def addNum(self, num: int) -> None:
        med = self.findMedian()

        # When we need to add a number if the number is > the median it goes in the min heap
        # if not it goes in the max heap, this will keep the median at the top of the heap to make finding it fat
        if num > med:
            heapq.heappush(self.nums_low, num)
        else:
            # python only supports a min heap so we make a max heap by converting all the numbers to negative
            heapq.heappush(self.nums_high, num * -1)

        # We need to balance the heap if one of the heaps ever exceeds the other heaps size by 1
        self.balanceHeap()
            
    def findMedian(self) -> float:
        # This base case is for checking for the median when adding a number and the heaps are empty
        if not self.nums_high and not self.nums_low:
            return 0
        
        # Whichever list has more will be the median if not its a sum of the top / 2.0 because we need to return a float
        if len(self.nums_low) < len(self.nums_high):
            return self.nums_high[0] * -1
            
        if len(self.nums_low) > len(self.nums_high):
            return self.nums_low[0]
        
        return ((self.nums_high[0] * -1) + self.nums_low[0]) / 2.0
    
    # We rebalance by taking the top of either heap and moving it to the other side
    # depending on which heap has exceeded the size of the other one by more than 1
    def balanceHeap(self) -> None:
        len_high = len(self.nums_high)
        len_low = len(self.nums_low)
        
        if len_high - len_low > 1:
            num = heapq.heappop(self.nums_high) * -1
            heapq.heappush(self.nums_low, num)
        elif len_low - len_high > 1:
            num = heapq.heappop(self.nums_low)
            heapq.heappush(self.nums_high, num * -1)
