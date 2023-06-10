class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        cache = collections.Counter()

        for start, end in intervals:
            cache[start] += 1
            cache[end] -= 1
        
        ans = cur = 0
        for time in sorted(cache.keys()):
            cur += cache[time]
            ans = max(ans, cur)

        return ans
