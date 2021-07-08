class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 把每格相同的記起來
        dp = collections.defaultdict(int)
        
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i, j] = dp[i-1, j-1] + 1
                    ans = max(ans, dp[i, j])
        
        return ans