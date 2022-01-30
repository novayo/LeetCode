class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}
        def recr(i1, i2, i3):
            if i3 >= len(s3):
                if i1 >= len(s1) and i2 >= len(s2):
                    return True
                else:
                    return False
            
            if (i1, i2, i3) in memo:
                return memo[i1, i2, i3]
            
            target = s3[i3]
            
            if i1 < len(s1) and s1[i1] == target:
                if recr(i1+1, i2, i3+1):
                    return True
            
            if i2 < len(s2) and s2[i2] == target:
                if recr(i1, i2+1, i3+1):
                    return True
            
            memo[i1, i2, i3] = False
            return memo[i1, i2, i3]
        
        return recr(0, 0, 0)
