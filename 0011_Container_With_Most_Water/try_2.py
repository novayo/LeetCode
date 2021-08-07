class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        ans = 0
        
        while i < j:                
            ans = max(ans, min(height[i], height[j])*(j-i)) # 計算面積
            
            # 將比較小的長度做移動
            left = height[i]
            right = height[j]
            if left <= right:
                while i < j and height[i] <= left:
                    i += 1
            else:
                while i < j and height[j] <= right:
                    j -= 1
        
        return ans
