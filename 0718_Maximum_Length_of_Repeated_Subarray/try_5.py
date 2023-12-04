class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        
        dp = [0] * (n2+1)
        
        ans = 0
        for i in range(n1-1, -1, -1):
            prev_right = [0] * (n2+1)
            for j in range(n2-1, -1, -1):
                prev_right[j] = dp[j]
                if nums1[i] == nums2[j]:
                    dp[j] = prev_right[j+1] + 1
                else:
                    dp[j] = 0
                
                ans = max(ans, dp[j])
        return ans

