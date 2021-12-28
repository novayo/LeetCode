class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}
        
        def count_conceution_one(state):
            ans = []
            for i, s in enumerate(state[:-1]):
                if state[i:i+2] == '++':
                    ans.append(i)
            return ans
            
        
        def stone_game(state, player):
            nonlocal memo
            
            if state in memo:
                return memo[state]
            
            
            valid_index = count_conceution_one(state)
            if not valid_index:
                memo[state] = False
                return memo[state]
            
            
            if player:
                for i in valid_index:
                    if not stone_game(state[:i] + '--' + state[i+2:], not player):
                        memo[state] = True
                        return memo[state]
                memo[state] = False
                return memo[state]
            
            else:
                for i in valid_index:
                    if not stone_game(state[:i] + '--' + state[i+2:], not player):
                        memo[state] = True
                        return memo[state]
                memo[state] = False
                return memo[state]
        
        return stone_game(currentState, True)