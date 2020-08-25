class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sort
        '''
        排序過後，去找下一個是否與自己相同
        時間複雜度：O(nlogn + n)
        空間複雜度：O(1)
        '''
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
