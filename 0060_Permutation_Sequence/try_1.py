class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = [str(i+1) for i in range(n)]
        
        for _ in range(k-1):
            i=j=n-1
            
            while i>0 and p[i-1] >= p[i]:
                i -= 1
            
            if i==0:
                p.reverse()
                continue
            i -= 1
            
            while j>0 and p[j] < p[i]:
                j -= 1
            
            p[i], p[j] = p[j], p[i]
            p[i+1:] = reversed(p[i+1:])
        
        return ''.join(p)
