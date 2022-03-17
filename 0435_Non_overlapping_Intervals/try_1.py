class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        choose = 1
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s >= end:
                choose += 1
                end = e
        return len(intervals) - choose