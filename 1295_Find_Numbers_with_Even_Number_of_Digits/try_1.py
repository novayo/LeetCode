class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        '''
        loop nums
        
        去找位數
        '''
        
        def getNumberOfdigit(target):
            # O(1)
            cnt = 0
            while target:
                target //= 10
                cnt += 1
            return cnt
        
        ret = 0
        for num in nums:
            if getNumberOfdigit(num) % 2 == 0:
                ret += 1
        return ret
