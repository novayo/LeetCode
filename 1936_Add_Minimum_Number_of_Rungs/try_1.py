class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        i = len(rungs) - 1
        ans = 0
        
        while i > 0:
            target = rungs[i] - dist
            
            if rungs[i-1] < target:
                ans += (rungs[i] - rungs[i-1] - 1) // dist
            i -= 1
        
        if rungs[0] - 0 > dist:
            ans += (rungs[i]-1) // dist
        return ans
