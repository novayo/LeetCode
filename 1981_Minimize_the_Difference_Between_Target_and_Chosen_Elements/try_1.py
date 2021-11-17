class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pre = set()
        
        # init
        for col in range(n):
            v = mat[0][col]
            pre.add(v)
        
        for i in range(1, m):
            tmp = set()
            first = 4900
            
            for col in range(n):
                v = mat[i][col]
                for p in pre:
                    if target <= v+p < first:
                        first = v+p
                    if v+p > first:
                        continue
                    tmp.add(v+p)
            
            for t in tmp.copy():
                if t > first:
                    tmp.remove(t)
            pre = tmp
        
        ans = float('inf')
        for v in pre:
            ans = min(ans, abs(v-target))
        return ans
