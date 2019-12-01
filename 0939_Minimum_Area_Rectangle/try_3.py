class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        _set, ans = set(), float('inf')
        for (x1, y1) in points:
            for (x2, y2) in _set:
                if (x1, y2) in _set and (x2, y1) in _set:
                    ans = abs(x2-x1)*abs(y2-y1) if abs(x2-x1)*abs(y2-y1) < ans else ans
            _set.add((x1, y1))
        
        return ans if ans != float('inf') else 0
