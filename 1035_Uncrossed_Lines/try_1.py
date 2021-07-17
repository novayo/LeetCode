class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1, length2 = len(nums1), len(nums2)
        dp = collections.defaultdict(int)
        
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i, j] = dp[i-1, j-1] + 1
                else:
                    dp[i, j] = max(dp[i, j-1], dp[i-1, j])
        
        return dp[length1, length2]
