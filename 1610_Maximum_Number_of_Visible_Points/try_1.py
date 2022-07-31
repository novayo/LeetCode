class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(x, y):
            return math.atan2(y-location[1], x-location[0])
        
        extra = 0
        angle_list = []
        for x, y in points:
            if [x, y] == location:
                extra += 1
                continue
            angle_list.append(getAngle(x, y))
        
        
        angle_list.sort()
        for _angle in angle_list.copy():
            angle_list.append(_angle + 2*math.pi)
        
        
        angle = angle / 180 * math.pi
        ans = i = 0
        for j in range(len(angle_list)):
            while i < j and angle_list[j] - angle_list[i] > angle:
                i += 1
            
            ans = max(ans, j-i+1)
        
        return ans + extra