class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        '''
        所有外角和加總=360
        
        計算所有  180-夾角(假設所有角度為內角) => 若加起來==360 => True
        若計算過程中>360 => return False
        '''
        
        def getAngle(middle, left, right):
            v1 = (left[0]-middle[0], left[1]-middle[1])
            v2 = (right[0]-middle[0], right[1]-middle[1])
            
            cos_theta = (v1[0]*v2[0]+v1[1]*v2[1]) / (math.sqrt((v1[0]**2+v1[1]**2)) * math.sqrt((v2[0]**2+v2[1]**2)))
            return math.degrees(math.acos(cos_theta))
        
        n = len(points)
        outside_angles = 0
        for i in range(n):
            outside_angles += 180-getAngle(points[i], points[i-1], points[(i+1) % n])
            if round(outside_angles, 5) > 360:
                return False
        return round(outside_angles, 5) == 360
