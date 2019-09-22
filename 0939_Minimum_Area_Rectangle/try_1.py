class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        visited = set()
        ans = 999999999
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    ans = abs(x2-x1) * abs(y2-y1) if abs(x2-x1) * abs(y2-y1) < ans else ans
            visited.add((x1, y1))
        return ans if ans != 999999999 else 0
