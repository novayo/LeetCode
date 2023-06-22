class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = sticks
        heapq.heapify(pq)

        ans = 0
        while len(pq) > 1:
            val1, val2 = heapq.heappop(pq), heapq.heappop(pq)
            new = val1 + val2
            ans += new
            heapq.heappush(pq, new)
        return ans
