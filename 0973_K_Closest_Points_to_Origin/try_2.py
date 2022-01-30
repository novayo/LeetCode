class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x**2 + y**2
        
        max_heap = []
        for x, y in points:
            d = distance(x, y)
            heapq.heappush(max_heap, (-d, (x, y)))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        for d, pos in max_heap:
            ans.append(pos)
        return ans
