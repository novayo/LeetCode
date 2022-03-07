class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def recr(l, r):
            
            if l > r:
                return False
            if l == r:
                return nums[l] == target
            
            mid = l + (r-l) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[r]:
                return recr(l, mid-1) or recr(mid+1, r)
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    return recr(mid+1, r)
                else:
                    return recr(l, mid-1)
            else:
                if nums[l] <= target < nums[mid]:
                    return recr(l, mid-1)
                else:
                    return recr(mid+1, r)
                
            
        return recr(0, len(nums)-1)