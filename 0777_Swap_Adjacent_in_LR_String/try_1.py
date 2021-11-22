class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        XL => LX => L 只能往左邊走
        RX => XR => R 只能往右邊走
        
        所以
        左邊的R一定要比右邊的R來的小
        左邊的L一定要比右邊的L來的大
        '''
        
        i, j = 0, 0
        
        while i < len(start) or j < len(end):
            while i < len(start) and start[i] == 'X':
                i += 1
            
            while j < len(end) and end[j] == 'X':
                j += 1
            
            if i >= len(start) and j >= len(end):
                break
            elif i >= len(start) and j < len(end):
                return False
            elif i < len(start) and j >= len(end):
                return False
            elif start[i] != end[j]:
                return False
            else:
                target = start[i]
                if target == 'L' and i < j:
                    return False
                elif target == 'R' and i > j:
                    return False
                else:
                    i += 1
                    j += 1
        return True
