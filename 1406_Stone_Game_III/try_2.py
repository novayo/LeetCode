class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}
        def next_player_max_score(index):
            if index >= n:
                return 0
            
            if index not in memo:
                memo[index] = -float('inf')
                for i in range(1, 4):
                    memo[index] = max(
                        memo[index], 
                        sum(stoneValue[index: index+i]) - next_player_max_score(index+i)
                    )
            return memo[index]
        
        ret = next_player_max_score(0)
        if ret > 0:
            return 'Alice'
        elif ret == 0:
            return 'Tie'
        else:
            return 'Bob'