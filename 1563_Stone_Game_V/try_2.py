class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # presum
        cur_sum = 0
        presum = [0] * (n+1)
        for i, v in enumerate(stoneValue):
            presum[i+1] += presum[i] + v
        
        # top down memo
        memo = {}
        def recr(l, r):
            if l >= r:
                return 0
            
            key = tuple(stoneValue[l:r+1])
            if key not in memo:
                ret = 0
                for i in range(l, r):
                    # left => l~i (include)    => presum[i+1] - presum[l]
                    left = presum[i+1] - presum[l]

                    # right => i+1, r (include)=> presum[r+1] - presum[i+1]
                    right = presum[r+1] - presum[i+1]

                    if left < right:
                        ret = max(ret, left + recr(l, i))
                    elif left > right:
                        ret = max(ret, right + recr(i+1, r))
                    else:
                        ret = max(ret, left + recr(l, i), right + recr(i+1, r))
                memo[key] = ret
            return memo[key]
        
        return recr(0, n-1)
                