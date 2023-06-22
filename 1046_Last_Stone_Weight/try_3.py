class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-v for v in stones]
        heapq.heapify(pq)
        
        while len(pq) > 1:
            v1, v2 = -heapq.heappop(pq), -heapq.heappop(pq)
            
            if v1 != v2:
                heapq.heappush(pq, -abs(v1-v2))
        
        return -pq[0] if pq else 0
        