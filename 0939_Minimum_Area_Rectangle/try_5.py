class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float('inf')
        n = len(points)
        points.sort()
        points_set = set([tuple(point) for point in points])
        
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 or y1 == y2 or y1 > y2:
                    continue
                
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    ans = min(ans, (y2-y1) * (x2-x1))
        
        return ans if ans < float('inf') else 0
