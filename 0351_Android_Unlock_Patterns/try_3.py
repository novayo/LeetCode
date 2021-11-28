class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        def isExist(bitmask, i):
            return (bitmask & 2**(i-1)) > 0
        
        def checkMiddle(x, y):
            if x > y:
                x, y = y, x
            return (x, y) in {(1,3),(1,7),(1,9),(3,7),(3,9),(7,9),(2,8),(4,6)}
        
        def dfs(i, step, maxStep, bitmask):
            nonlocal ans
            
            bitmask |= 2**(i-1)
            
            if (bitmask, i) in memo:
                return memo[bitmask, i]
            
            if step == maxStep:
                return 1
            
            cur = 0
            for neighbor in range(1, 10):
                if isExist(bitmask, neighbor) or (checkMiddle(i, neighbor) and isExist(bitmask, (i+neighbor) // 2) == False):
                    continue
                
                cur += dfs(neighbor, step+1, maxStep, bitmask)
            
            memo[bitmask, i] = cur
            return cur
            
            
        
        ans = 0
        for maxStep in range(m, n+1):
            memo = {}
            for i in range(1, 10):
                ans += dfs(i, 1, maxStep, 0)
        
        return ans