class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        def compare(x, y):
            if x > y:
                x, y = y, x
            return (x, y) in {(1, 7), (1, 3), (1, 9), (3, 9), (3, 7), (7, 9), (4, 6), (2, 8)}
        
        def dfs(i, step, bitmap, maxStep, found):
            bitmap += 2**(i-1)
            
            if step == maxStep:
                return 1
            
            if (bitmap, i) in memo:
                return memo[bitmap, i]
            
            cur = 0
            for x in range(1, 10):
                if x in found or (compare(i, x) and (i+x)//2 not in found):
                    continue
                found.add(x)
                cur += dfs(x, step+1, bitmap, maxStep, found)
                found.remove(x)
            
            memo[bitmap, i] = cur
            return cur
        
        ans = 0
        for maxStep in range(m, n+1):
            memo = {}
            for i in range(1, 10):
                ans += dfs(i, 1, 0, maxStep, set([i]))
        return ans