class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 每次都跳最遠，去紀錄最遠的index
        farthest_index = 0
        
        for i, num in enumerate(nums):
            farthest_index = max(farthest_index, i+num)
            
            # 如果這格跳完了，還是留在原地，那就表示從一開始到現在都最遠只能跳到這格
            # 檢查是否跳到最後一格
            if i == farthest_index:
                return i == len(nums)-1
        
        return True
        
