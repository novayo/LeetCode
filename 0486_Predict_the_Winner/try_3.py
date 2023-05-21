class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache
        def maxP1Score(player1, i, j):
            if i > j:
                return 0
            
            if player1:
                ret = max(maxP1Score(False, i+1, j) + nums[i], maxP1Score(False, i, j-1) + nums[j])
            else:
                ret = min(maxP1Score(True, i+1, j), maxP1Score(True, i, j-1))
            
            return ret
        
        p1 = maxP1Score(True, 0, len(nums)-1)
        p2 = sum(nums) - p1
        return p1 >= p2
        
