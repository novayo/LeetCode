class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # time comp: O(nlogn + nlogk)
        # space comp: O(n+k)
        sorted_list = sorted([(w/q, q) for q, w in zip(quality, wage)], reverse=True)
        pq = []
        cur_pq_sum = cur_max_ratio = 0
        ans = float('inf')
        
        for i in range(len(sorted_list)-1, -1, -1):
            new_ratio, q = sorted_list[i]
            if len(pq) >= k:
                cur_pq_sum += heapq.heappop(pq)
            
            if len(pq) < k:
                heapq.heappush(pq, -q)
                cur_pq_sum += q
                cur_max_ratio = new_ratio
            
            if len(pq) >= k:
                ans = min(ans, cur_pq_sum * cur_max_ratio)
        return ans
