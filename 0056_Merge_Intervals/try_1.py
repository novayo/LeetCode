class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        start, end, ans = intervals[0][0], intervals[0][1], collections.deque()
        
        for v in intervals[1:]:
            if v[0] > v[1]:
                continue
            if end < v[0]:
                ans.append([start, end])
                start = v[0]
                end = v[1]
            elif end >= v[0] and end < v[1]:
                end = v[1]
        ans.append([start,end])
        return ans
