class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort()
        ans = collections.deque()
        ans.append(intervals[0])
        
        for v in intervals[1:]:
            if ans[-1][1] < v[0]:
                ans.append(v)
            elif ans[-1][1] >= v[0] and ans[-1][1] < v[1]:
                ans[-1][1] = v[1]
        return ans
