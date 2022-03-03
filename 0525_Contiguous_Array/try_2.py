class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        遇到1的時候+1，0的時候-1
        
        [....3........3.....]
        第一個3表示: 從0開始往後計算
        第二個3表示: 從0開始往後計算
        此時第一個3~第二個3之前就是 答案
        '''
        ans = counter = 0
        table = {0: -1}
        for i, num in enumerate(nums):
            counter += 1 if num == 1 else -1
            if counter in table:
                ans = max(ans, i-table[counter])
            else:
                table[counter] = i
        return ans