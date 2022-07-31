class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @functools.lru_cache(None)
        def recr(val):
            if val == 1:
                return 0
            
            if val % 2 == 0:
                return 1 + recr(val // 2)
            else:
                return 1 + recr(3*val + 1)
        
        max_heap = []
        for i in range(lo, hi+1):
            heapq.heappush(max_heap, (-recr(i), -i))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return -max_heap[0][1]
