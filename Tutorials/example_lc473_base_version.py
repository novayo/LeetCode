class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        分成四等分，每一份一樣長
        '''
        def recr(idx, s1, s2, s3, s4):
            if idx >= len(matchsticks):
                return s1 == s2 == s3 == s4
            
            
            return recr(idx + 1, s1 + matchsticks[idx], s2, s3, s4) \
                    or recr(idx + 1, s1, s2 + matchsticks[idx], s3, s4) \
                    or recr(idx + 1, s1, s2, s3 + matchsticks[idx], s4) \
                    or recr(idx + 1, s1, s2, s3, s4 + matchsticks[idx])
        
        return recr(0, 0, 0, 0, 0)
        
