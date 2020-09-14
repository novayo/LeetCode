class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        '''
        用長度去測試，範圍：0~len(s)/2
        '''
        
        len_s = len(s)
        for length in range(1, len_s//2+1):
            if len_s % length == 0:
                ans = s[:length] * (len_s // length)
                if ans == s:
                    return True
                
        return False
