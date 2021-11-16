class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        '''
        a = s1s1s2s2
        b = s2s2s1s1
        
        a => 多*1次才能找出所有的b
        '''
        times = ceil(len(b) / len(a))
        
        if b in a*(times):
            return times
        elif b in a*(times+1):
            return times+1
        else:
            return -1
