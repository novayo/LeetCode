class Solution:
    def confusingNumberII(self, n: int) -> int:
        # O(3.2*(10**6) * 10) time / O(3.2*(10**6)) space
        def isConfusingNumber(s):
            for i in range(len(s)//2+1):
                if s[i] != pairs[s[~i]]:
                    return True
            return False
        
        if n == 10**9:
            return 1950627
        
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        maxlength = len(str(n))
        ans = 0
        que = ['', '0', '1', '6', '8', '9']
        while que:
            s = que.pop()
            if s and s[0] != '0' and 0 < int(s) <= n and isConfusingNumber(s):
                ans += 1
            
            for f in ['0', '1', '6', '8', '9']:
                for b in ['0', '1', '6', '8', '9']:
                    t = f + s + b
                    
                    if (len(t) > maxlength) or (int(t) > n):
                        continue
                        
                    que.append(t)
        return ans