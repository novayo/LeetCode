class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        '''
        LC153 的進階版
        
        一樣直接從中間切下去
        * 右邊比中間大：45123
        * 右邊比中間小：34512
        
        有個問題，如果是一般的binary search的話，
        下面這兩個例子都會抓到nums[1] = 3，
        但是一個是要找右邊，一個是要找左邊
        [3,3,1,3]
        [1,3,3]
        '''
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
