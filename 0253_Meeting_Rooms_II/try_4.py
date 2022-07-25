class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ans = 0
        min_heap = []
        for s, e in intervals:
            while min_heap and min_heap[0] <= s:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, e)
            ans = max(ans, len(min_heap))
        return ans
