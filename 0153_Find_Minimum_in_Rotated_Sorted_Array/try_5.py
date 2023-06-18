class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 如果沒有rotate
        if nums[0] < nums[-1]:
            return nums[0]
        
        ans = -1
        i, j = 0, len(nums)-1
        while i <= j:
            mid = i + (j-i) // 2
            
            # 代表還在左半邊
            if nums[mid] >= nums[0]:
                i = mid+1
            
            # 代表在右半邊了
            elif nums[mid] < nums[0]:
                ans = mid
                j = mid-1
            
        return nums[ans]
                
            
