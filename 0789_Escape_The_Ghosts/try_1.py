class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(pos):
            return abs(pos[0]-target[0]) + abs(pos[1]-target[1])
        
        d1 = dist([0,0])
        for g in ghosts:
            if d1 >= dist(g):
                return False
        return True
