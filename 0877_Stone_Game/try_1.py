class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        Alex選完之後，Lee亂選的所有可能，Alex都要獲勝，Alex才算獲勝
              memo = {(flag, i, j): True or False}
        Alex turn:
            if piles[i] > piles[j]:
                if recr(not flag, A+piles[i], L, i+1, j): # 如果有找到一組是True的，就代表走這個可能就可以了，因此直接return
                    memo[現在位置] = True
                    return True
            elif piles[i] < piles[j]:
                if recr(not flag, A+piles[j], L, i, j-1):
                    memo[現在位置] = True
                    return True
            else:
                if recr(not flag, A+piles[i], L, i+1, j) or recr(not flag, A+piles[j], L, i, j-1):
                    memo[現在位置] = True
                    return True
            memo[現在位置] = False 
        Lee turn:
            if recr(not flag, A, L+piles[i], i+1, j) or recr(not flag, A, L+piles[j], i, j-1):
                memo[現在位置] = True
                return True
            memo[現在位置] = False
        '''  
        
        def recr(flag, A, L, i, j, memo={}):
            if (flag, i, j) in memo:
                return memo[flag, i, j]
            
            if i > j or i >= len(piles) or j < 0:
                memo[flag, i, j] = A > L
                return A > L
            
            if flag:
                if piles[i] > piles[j]:
                    if recr(not flag, A+piles[i], L, i+1, j, memo): # 如果有找到一組是True的，就代表走這個可能就可以了，因此直接return
                        memo[flag, i, j] = True
                        return True
                elif piles[i] < piles[j]:
                    if recr(not flag, A+piles[j], L, i, j-1, memo):
                        memo[flag, i, j] = True
                        return True
                else:
                    if recr(not flag, A+piles[i], L, i+1, j, memo) or recr(not flag, A+piles[j], L, i, j-1, memo):
                        memo[flag, i, j] = True
                        return True
                memo[flag, i, j] = False 
            else:
                if recr(not flag, A, L+piles[i], i+1, j, memo) or recr(not flag, A, L+piles[j], i, j-1, memo):
                    memo[flag, i, j] = True
                    return True
                memo[flag, i, j] = False
            return False
        
        return recr(True, 0, 0, 0, len(piles)-1)
