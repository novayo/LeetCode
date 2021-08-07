class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        _min = float('inf')
        
        # 紀錄所有位置的 左邊最小
        _min_list = []
        for num in nums:
            _min = min(_min, num)
            _min_list.append(_min)
        
        # 紀錄右邊比中間大的值，較小的值就拿來跟當前位置的左邊最小去做比較
        stack = [-float(inf)]
        for i in range(len(nums)-1, -1, -1):
            left = _min_list[i]
            mid = nums[i]
            right = stack[-1]
            
            while mid > right:
                if right > left:
                    return True
                stack.pop() # 將left > right的刪除
                if not stack:
                    break
                right = stack[-1]
            
            stack.append(mid)
        return False
