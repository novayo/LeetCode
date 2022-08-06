class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @functools.lru_cache(None)
        def recr(candidate):
            if candidate == 1:
                return 0
            
            if candidate % 2 == 0:
                return 1 + recr(candidate // 2)
            else:
                return 1 + recr(candidate * 3 + 1)
        
        tmp = []
        pq = []
        for candidate in range(lo, hi+1):
            tmp.append(recr(candidate))
            heapq.heappush(pq, (-recr(candidate), -candidate))
            
            if len(pq) > k:
                heapq.heappop(pq)
        return -pq[0][1]
