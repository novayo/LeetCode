class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        if xCenter < x1:
            most_closest_x = x1
        elif xCenter > x2:
            most_closest_x = x2
        else:
            most_closest_x = xCenter
            
        if yCenter < y1:
            most_closest_y = y1
        elif yCenter > y2:
            most_closest_y = y2
        else:
            most_closest_y = yCenter
        
        return radius ** 2 >= ((most_closest_x - xCenter) ** 2 + (most_closest_y - yCenter) ** 2)