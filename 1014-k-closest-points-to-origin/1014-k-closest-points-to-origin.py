class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x = point[0]
            y = point[1]
            return x * x + y * y

        # Use a min-heap to store the points based on their distance
        h = []
        for point in points: # n 
            d = distance(point)
            heapq.heappush(h, (d, point)) # heap size: n

        # Extract the k closest points
        res = []
        for i in range(k): # k
            first_pt_d, first_pt = heapq.heappop(h) # heap size: n
            res.append(first_pt)
        return res
