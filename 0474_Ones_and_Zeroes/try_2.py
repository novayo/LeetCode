class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        bottom-up 找出所有可能，過程中不能超過題目要求
        '''
        
        ans = 0
        
        def recr(index):
            nonlocal ans
            if index >= len(strs):
                return set([(0, 0, 0)]) # 0, 1, len
            
            counter = Counter(strs[index])
            ret = recr(index+1)
            for zero, one, length in ret.copy():
                _zero, _one = zero+counter['0'], one+counter['1']
                if _zero <= m and _one <= n:
                    ret.add((_zero, _one, length+1))
                    ans = max(ans, length+1)
            return ret
        
        recr(0)
        return ans

