class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        建立一個list長度為三
        由大到小排序
        之後直接去比較，
        如果a>[0]，則第一二個向右移，第一個變成a
        如果a>[1]，則第二個向右移，第二個變成a
        如果a>[2]，則第三個變成a
        如果[2]>a，則不變
        
        回傳[-1]
        '''
        if len(nums) == 0:
            return -float('inf')
        if len(nums) < 3:
            return max(nums)
        
        ans = [-float('inf'),-float('inf'),-float('inf')]
        for num in nums:
            if num == ans[0] or num == ans[1] or num == ans[2]:
                continue
                
            if num > ans[0]:
                ans[1], ans[2] = ans[0], ans[1]
                ans[0] = num
            elif num > ans[1]:
                ans[2] = ans[1]
                ans[1] = num
            elif num > ans[2]:
                ans[2] = num
        
        if ans[-1] == -float('inf'):
            return ans[0]
        else:
            return ans[-1]
