class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(flag, i, j, A=0, B=0):
            
            if i > j:
                if flag:
                    memo[flag, i, j] = A >= B
                else:
                    memo[flag, i, j] = A < B
                return memo[flag, i, j]
            
            if flag:
                if not dfs(not flag, i+1, j, A+nums[i], B) or not dfs(not flag, i, j-1, A+nums[j], B):
                    memo[flag, i, j] = True
                    return memo[flag, i, j]
            else:
                if not dfs(not flag, i+1, j, A, B+nums[i]) or not dfs(not flag, i, j-1, A, B+nums[j]):
                    memo[flag, i, j] = True
                    return memo[flag, i, j]
            
            memo[flag, i, j] = False
            return memo[flag, i, j]
        
        return dfs(True, 0, len(nums)-1)
