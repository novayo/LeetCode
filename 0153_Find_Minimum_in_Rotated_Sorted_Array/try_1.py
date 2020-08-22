class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        '''
        從中間切下去，這樣分成兩種情況
        第一種，45123，左邊大於中間，right = mid
        第二種，345612，左邊小於中間，left = mid
        '''
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[left] > nums[mid]:
                right = mid
            else:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                else:
                    left = mid+1
        return nums[left] if nums[left] < nums[0] else nums[0]
