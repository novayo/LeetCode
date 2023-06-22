class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        pq = nums
        heapq.heapify(pq)
        
        ans = subtract = 0
        while pq:
            while pq and pq[0] <= subtract:
                heapq.heappop(pq)
            
            if not pq:
                break
            
            smallest = heapq.heappop(pq)
            diff = smallest - subtract
            subtract += diff
            ans += 1

        return ans
        