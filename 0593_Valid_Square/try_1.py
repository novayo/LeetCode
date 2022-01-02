class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        找對角線
            - 找一點xy互斥的
        '''
        
        def dist(pos1, pos2):
            return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2
        
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        
        side1_1 = dist(p1, p2)
        side1_2 = dist(p1, p3)
        diagonal1 = dist(p1, p4)
        
        side2_1 = dist(p4, p3)
        side2_2 = dist(p4, p2)
        diagonal2 = dist(p2, p3)
        
        if side1_1 == side1_2 == side2_1 == side2_2 and diagonal1 == diagonal2:
            return True
        else:
            return False

