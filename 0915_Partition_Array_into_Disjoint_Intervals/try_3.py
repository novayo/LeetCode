class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ''' https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/1354396/Python-From-O(N)-space-to-O(1)-space-Picture-explained-Clean-and-Concise
        '''
        left_min = right_max = nums[0]
        ans = 0
        
        for i in range(1, len(nums)):
            right_max = max(right_max, nums[i])
            
            # 若有新的比較小的值，則目前左邊最大更新成目前最大
            if nums[i] < left_min:
                ans = i
                left_min = right_max
        
        return ans + 1
