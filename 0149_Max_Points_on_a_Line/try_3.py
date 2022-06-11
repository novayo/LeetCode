class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_line(p1, p2):
            # y = mx + b
            if p1[0] == p2[0]:
                return float('inf'), p1[0]
                
            m = (p1[1] - p2[1]) / (p1[0] - p2[0])
            b = p1[1] - m * p1[0]
            return m, b
        
        ans = 1
        cache = collections.defaultdict(set)
        n = len(points)
        points.sort()
        
        for i in range(n-1):
            for j in range(i+1, n):
                count = 2
                m, b = get_line(points[i], points[j])
                if tuple(points[i]) in cache[m, b] and tuple(points[j]) in cache[m, b]:
                    continue
                cache[m, b].add(tuple(points[i]))
                cache[m, b].add(tuple(points[j]))
                
                for k in range(j+1, n):
                    _m, _b = get_line(points[i], points[k])
                    cache[_m, _b].add(tuple(points[k]))
                    if m == _m and b == _b:
                        count += 1
                
                ans = max(ans, count)
        return ans
