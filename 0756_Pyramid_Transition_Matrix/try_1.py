class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        '''
        n = len(bottom)
        m = len(allowed)
        1. 檢查allowed的數量夠不夠擺 => if n*(n-1) // 2 <= m
        2. 用底層分類
        3. 紀錄當前的row是誰，並遞迴去找，若len(row) == 1，則return True
        '''
        
        n = len(bottom)
        m = len(allowed)
        
        # If blocks are not enough
        if n*(n-1) // 2 > m:
            return False
        
        # category
        table = collections.defaultdict(set)
        for block in allowed:
            table[block[:2]].add(block[2])
        
        # recursion
        memo = {}
        def recr(bottom, start_index, next_bottom):

            if len(bottom) == 1:
                return True
            
            if start_index == len(bottom)-1:
                return recr(next_bottom, 0, '')
            
            if (bottom, start_index, next_bottom) not in memo:
                for top in table[bottom[start_index:start_index+2]]:
                    if recr(bottom, start_index+1, next_bottom+top):
                        return True
                memo[bottom, start_index, next_bottom] = False
            return memo[bottom, start_index, next_bottom]
        
        return recr(bottom, 0, '')
