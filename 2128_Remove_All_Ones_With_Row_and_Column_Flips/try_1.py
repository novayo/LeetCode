class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        invert_r1 = [0 if v == 1 else 1 for v in grid[0]]
        
        for row in grid[1:]:
            if row != r1 and row != invert_r1:
                return False
        return True
