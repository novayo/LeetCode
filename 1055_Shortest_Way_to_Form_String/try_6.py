class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = j = 0
        
        while j < len(target):
            ans += 1
            hit = False
            for s in source:
                if s == target[j]:
                    hit = True
                    j += 1
                    if j >= len(target):
                        break
            
            if not hit:
                return -1
        return ans
