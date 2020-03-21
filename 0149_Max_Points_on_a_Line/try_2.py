class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)<=2): 
            return len(points)
            
        ans = 0
        for i in range(len(points)-1):
            dict = {}
            count = 1
            duplicate = 0
            horizontal = 1
            for j in range(i+1, len(points)):
                if points[i]==points[j]:
                    duplicate += 1
                elif points[i][1]==points[j][1]:
                    horizontal += 1
                    count = max(count, horizontal)
                else:
                    m = (points[i][0]-points[j][0]) / (points[i][1]-points[j][1])
                    dict[m]  = dict.get(m, 1) + 1
                    count = max(count, dict[m])
            ans = max(ans, count+duplicate)
        
        return ans
