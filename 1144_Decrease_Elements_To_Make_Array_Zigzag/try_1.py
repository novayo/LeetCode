class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ans = float('inf')
        
        # 大小大, 小大小
        for a, b in [0, 1], [1, 0]:
            prev = nums[0]
            move = 0
            for i, num in enumerate(nums):
                if i == 0:
                    continue

                if i % 2 == a and prev >= num:
                    move += prev-num+1
                    prev = num
                elif i % 2 == b and prev <= num:
                    move += num-prev+1
                    prev = prev-1
                else:
                    prev = num
            ans = min(ans, move)
        
        return ans