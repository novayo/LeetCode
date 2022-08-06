class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(P1, P2):
            return (P1[0]-P2[0]) ** 2 + (P1[1]-P2[1]) ** 2
        
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        if dist(p1, p2) == dist(p1, p3) == dist(p2, p4) == dist(p3, p4) and dist(p1, p4) == dist(p2, p3):
            return True
        return False
        