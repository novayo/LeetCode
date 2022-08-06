class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        used_rooms = []
        
        for s, e in sorted(intervals):
            while used_rooms and used_rooms[0] <= s:
                heapq.heappop(used_rooms)
            
            heapq.heappush(used_rooms, e)
            ans = max(ans, len(used_rooms))
        return ans
