class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def recr(i, num_0, num_1):
            if i >= len(strs):
                return 0
        
            counter = collections.Counter(strs[i])
            
            ans = recr(i+1, num_0, num_1)
            if num_0 + counter["0"] <= m and num_1 + counter["1"] <= n:
                ans = max(ans, 1 + recr(i+1, num_0 + counter["0"], num_1 + counter["1"]))
            return ans
        
        return recr(0, 0, 0)
