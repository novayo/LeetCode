class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = [0] * (10**6 + 1)

        for start, end in intervals:
            arr[start] += 1
            arr[end] -= 1
        
        ans = cur = 0
        for num in arr:
            cur += num
            ans = max(ans, cur)

        return ans
