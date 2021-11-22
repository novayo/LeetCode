class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        '''
        找到對角線，就可以決定另外兩個點
        '''
        point_set = set()
        for x, y in points:
            point_set.add((x, y))
        
        points.sort()
        ans = float('inf')
        
        for i in range(len(points)):
            
            base = points[i]
            
            for j in range(i+1, len(points)):
                diagonal = points[j]
                
                if base[0] == diagonal[0] or base[1] == diagonal[1] or base[1] > diagonal[1]:
                    continue
                
                left_up_point = (base[0], diagonal[1])
                right_down_point = (diagonal[0], base[1])
                
                if left_up_point not in point_set or right_down_point not in point_set:
                    continue
                    
                ans = min(ans, abs(base[0]-diagonal[0]) * abs(base[1]-diagonal[1]))
        
        return 0 if ans == float('inf') else ans
