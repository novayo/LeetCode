class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        def p1Win(player1, i, j, p1, p2):
            if i > j:
                return p1 >= p2
            
            if (player1, i, j, p1, p2) not in memo:
                if player1:
                    memo[player1, i, j, p1, p2] = p1Win(False, i+1, j, p1+nums[i], p2) \
                                                  or p1Win(False, i, j-1, p1+nums[j], p2)
                else:
                    memo[player1, i, j, p1, p2] = p1Win(True, i+1, j, p1, p2+nums[i]) \
                                                  and p1Win(True, i, j-1, p1, p2+nums[j])
            return memo[player1, i, j, p1, p2]
        
        return p1Win(True, 0, len(nums)-1, 0, 0)
                       