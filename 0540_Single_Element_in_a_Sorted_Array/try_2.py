class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        binary search left => check if the length from start to current index is odd or even
        if odd, answer locates in left side
        otherwise, right side
        
        if index != index + 1 => find answer
            care about edge case
        '''
        
        l, r = 0, len(nums)-1
        ans = -1
        while l < r:
            mid = l + (r-l) // 2
            
            if nums[mid] == nums[mid-1]:
                mid -= 1
            elif nums[mid] == nums[mid+1]:
                pass
            else:
                l = mid
                break
            
            if mid % 2 == 0:
                l = mid + 2
            else:
                r = mid - 1
                
        return nums[l]
