class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        '''
        從中間切下去，這樣分成兩種情況
        第一種，45123，右邊大於中間，right = mid
        第二種，345612，右邊小於中間，left = mid + 1
        '''
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
