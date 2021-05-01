class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        只要有數字，一定走得到結尾
        因此只要尋找0，看是否目前"最遠到達index"能否超越此位置即可，且此位置不能為最後一位
        '''
        
        cur_max_index = 0
        
        for i in range(len(nums)-1): # 最後一位不考慮
            cur_max_index = max(cur_max_index, i + nums[i]) # 每次更新"最遠到達index"最大值
            if nums[i] == 0 and cur_max_index <= i: # 若"最遠到達index"不能超越目前0
                return False
            
        return True
