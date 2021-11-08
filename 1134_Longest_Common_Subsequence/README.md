Question: https://leetcode.com/problems/longest-common-subsequence/

---

try_1.py: O(m*n) O(m*n)
* Runtime: 408 ms, faster than 87.36% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 21.6 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.

> dp

---

try_2.py: O(m*n) O(m*n)

* Runtime: 348 ms, faster than 94.18% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 21.9 MB, less than 85.70% of Python3 online submissions for Longest Common Subsequence.

> dp[i][j] = text1[:i] & text2[:j] 有幾個相同
> if text1[i] == text2[j] => dp[i-1][j-1] + 1 (各前一位+1)
> else => 取前幾種狀況最大即可 max(dp[i-1][j], dp[i][j-1])

