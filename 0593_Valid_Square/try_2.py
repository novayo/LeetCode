class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        p2 p4
        p1 p3
        '''
        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        
        p1, p2 , p3, p4 = sorted([p1, p2, p3, p4])
        
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        return dist(p1, p2) == dist(p1, p3) == dist(p4, p2) == dist(p4, p3) and dist(p1, p4) == dist(p2, p3)
