class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = j = 0
        
        ans = 0
        pre = -1
        while j < len(target):
            pre = j
            
            for s in source:
                if j >= len(target):
                    break
                if target[j] == s:
                    j += 1
            
            if pre == j:
                return -1
            
            ans += 1
        
        return ans
                
            
