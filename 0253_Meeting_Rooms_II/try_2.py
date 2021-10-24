class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ans = 0
        heap = []
        for start, end in intervals:
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            ans = max(ans, len(heap))
        
        return ans