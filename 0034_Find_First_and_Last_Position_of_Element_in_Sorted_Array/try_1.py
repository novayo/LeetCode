class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        
        if not nums:
            return ans
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l+r) // 2
            
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        print(l, r)
        if nums[l] == target:
            ans[0] = l
        
        r = len(nums)
        while l < r:
            mid = (l+r) // 2
            
            if nums[mid] != target:
                r = mid
            elif mid < len(nums)-1 and nums[mid+1] == target:
                l = mid + 1
            else:
                l = mid
                break
        print(l, r)
        if nums[l] == target:
            ans[1] = l
        
        return ans
        
