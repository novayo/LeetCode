class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        bottom-up 找出所有可能，過程中不能超過題目要求
        '''
        
        ans = 0
        
        dp = set([(0, 0, 0)])
        
        for index in range(len(strs)-1, -1, -1):
            counter = Counter(strs[index])
            for zero, one, length in dp.copy():
                _zero, _one = zero+counter['0'], one+counter['1']
                if _zero <= m and _one <= n:
                    dp.add((_zero, _one, length+1))
                    ans = max(ans, length+1)
        return ans
