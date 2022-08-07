class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = float('inf')
        
        points_set = set()
        for i in range(n):
            points_set.add(tuple(points[i]))
        
        points.sort()
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                
                if x1 == x2 or y1 == y2 or y1 > y2:
                    continue
                
                x3, y3 = x1, y2
                x4, y4 = x2, y1
                
                if (x3, y3) in points_set and (x4, y4) in points_set:
                    ans = min(ans, (x2-x1) * (y2-y1))
        
        return ans if ans < float('inf') else 0
                
