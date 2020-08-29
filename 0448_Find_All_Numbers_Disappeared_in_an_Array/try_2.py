class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        因為是1~len(nums)
        故，將找過的位置改成 負的 即可
        之後要取用的話，就轉成正的來取用
        剩下正的位置就是沒有的值
        '''
        
        for num in nums:
            num = abs(num) - 1
            
            if nums[num] > 0:
                nums[num] *= -1
        
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
