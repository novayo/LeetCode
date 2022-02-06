class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x**2 + y**2
        
        max_heap = []
        for x, y in points:
            dist = distance(x, y)
            heapq.heappush(max_heap, (-dist, x, y))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        for dist, x, y in max_heap:
            ans.append([x, y])
        return ans
