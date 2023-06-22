class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ans = 0
        pq = []
        for s, e in intervals:
            while pq and pq[0] <= s:
                heapq.heappop(pq)
            
            heapq.heappush(pq, e)
            ans = max(ans, len(pq))
        
        return ans