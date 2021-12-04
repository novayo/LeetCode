class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def getLength(pos1, pos2):
            x1,y1 = pos1
            x2,y2 = pos2
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        
        n = len(points)
        
        center_pair = collections.defaultdict(list)
        for i in range(n):
            x_1, y_1 = points[i]
            
            for j in range(i+1, n):
                x_2, y_2 = points[j]
                mid_x, midy = (x_1+x_2)/2, (y_1+y_2)/2
                d = getLength(points[i],points[j])
                center_pair[(mid_x, midy, d)].append(((x_1,y_1), (x_2,y_2)))
                
        
        ans = float('inf')
        for key, items in center_pair.items():
            for i in range(len(items)):
                o1 = items[i][0]
                for j in range(len(items)):
                    if i == j:
                        continue
                    point1, point2 = items[j]
                    len1 = getLength(o1, point1)
                    len2 = getLength(o1, point2)
                    ans = min(ans, len1*len2)

        return 0 if ans == float('inf') else ans
