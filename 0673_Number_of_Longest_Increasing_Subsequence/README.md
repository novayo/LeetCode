Question: https://leetcode.com/problems/number-of-longest-increasing-subsequence/

---

try_1.py: O(n^2) O(n)

* Runtime: 1156 ms, faster than 86.66% of Python3 online submissions for Number of Longest Increasing Subsequence.
* Memory Usage: 14.9 MB, less than 8.43% of Python3 online submissions for Number of Longest Increasing

> dp[i][0] => s[i:] 的最大長度
> dp[i][1] => 目前總共有幾組
> i-1 => 找nums[i] < nums[i~n] 的dp[j][0]的最大並統計dp[j][1]