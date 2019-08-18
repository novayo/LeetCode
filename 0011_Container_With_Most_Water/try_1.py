class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxh, ans, i, j = max(height), 0, 0, len(height)-1
        
        for k in range(len(height)-1, 0, -1):
            if ans / k > maxh:
                break
            if height[i] < height[j]:
                if height[i] * k > ans:
                    ans = height[i] * k
                i += 1
            else:
                if height[j] * k > ans:
                    ans = height[j] * k
                j -= 1
        return ans
