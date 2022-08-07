class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        attempt1 = tuple(grid[0])
        attempt2 = tuple([1 if v == 0 else 0 for v in grid[0]])
        
        for i in range(1, len(grid)):
            attempt = tuple(grid[i])
            if attempt != attempt1 and attempt != attempt2:
                return False
        return True
