class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def special_case(a, b, k):
            dulp, o_k = 1, k
            while k < a:
                for _k in range(1, min(k, b-o_k)):
                    if a-k == o_k+_k and a-k+_k == b-o_k-_k and k-_k == b-o_k:
                        return dulp+4
                
                dulp += 1
                k += k
            return float('inf')
            
        
        memo = {}
        
        def dfs(a, b):
            if a == b:
                return 1
            if a <= 0 or b <= 0:
                return 0
            
            if b > a:
                a, b = b, a
            
            if (a, b) not in memo:
                ret = float('inf')
                for k in range(b, 0, -1):
                    ret = min(
                        ret, 
                        1 + dfs(k, a-k) + dfs(b-k, a),
                        1 + dfs(b, a-k) + dfs(b-k, k),
                        1 + dfs(k, a-k) + dfs(a-k, b-k) + dfs(b-k, k),
                        special_case(a, b, k)
                     )
                    
                memo[a, b] = ret
            return memo[a, b]
        
        return dfs(n, m)