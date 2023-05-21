class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        分成四等分，每一份一樣長
        '''
        _sum = sum(matchsticks)
        if _sum % 4 != 0:
            return False
        equal = _sum // 4
        
        
        matchsticks.sort(reverse=True)
        def recr(idx, s1, s2, s3, s4):
            if idx >= len(matchsticks):
                return s1 == s2 == s3 == s4
            
            if s1 > equal or s2 > equal or s3 > equal or s4 > equal:
                return False
            
            return recr(idx + 1, s1 + matchsticks[idx], s2, s3, s4) \
                    or recr(idx + 1, s1, s2 + matchsticks[idx], s3, s4) \
                    or recr(idx + 1, s1, s2, s3 + matchsticks[idx], s4) \
                    or recr(idx + 1, s1, s2, s3, s4 + matchsticks[idx])
        
        return recr(0, 0, 0, 0, 0)
