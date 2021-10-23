class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def getMaxProduct(i, j):
            if i > j:
                return 0
            elif i == j:
                return nums[i]
            left = right = total = 1
            
            hitFirstNeg = False
            for k in range(i, j+1):
                total *= nums[k]
                
                # 紀錄第一個負之前的乘積 => 遇到第一個負停止計算
                if hitFirstNeg == False:
                    left *= nums[k]
                    if nums[k] < 0:
                        hitFirstNeg = True
                
                # 紀錄最後一個負的乘積 => 遇到第一個負開始計算
                if hitFirstNeg == True:
                    right *= nums[k]
                    if nums[k] < 0:
                        right = nums[k]
            
            return max(total, total // left, total // right)
        
        i = j = 0
        ans = -float('inf')
        while j < len(nums):
            while j < len(nums) and nums[j] != 0:
                j += 1
            
            ans = max(ans, getMaxProduct(i, j-1))
            if j < len(nums) and nums[j] == 0:
                ans = max(ans, 0)
            i = j = j+1
        return ans