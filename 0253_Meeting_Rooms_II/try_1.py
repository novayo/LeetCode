class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        ans = 1
        heap = []
        heapq.heappush(heap, (intervals[0][1], intervals[0][0])) # min-heap
        
        for i in range(1, len(intervals)):
            min_end, _ = heap[0]
            
            start, end = intervals[i]
            
            if min_end <= start:
                while heap and heap[0][0] <= intervals[i][0]:
                    heapq.heappop(heap)
                
            heapq.heappush(heap, (intervals[i][1], intervals[i][0]))
            ans = max(ans, len(heap))
        
        return ans
