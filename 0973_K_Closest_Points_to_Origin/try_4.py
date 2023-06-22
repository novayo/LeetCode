class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(pq, (-dist, x, y))
            if len(pq) > k:
                heapq.heappop(pq)
        
        return [[arr[1], arr[2]] for arr in pq]
