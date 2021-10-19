Question: https://leetcode.com/problems/longest-palindromic-subsequence/

---

try_1.py: O(n^2) O(n^2)

* Runtime: 2811 ms, faster than 33.13% of Python3 online submissions for Longest Palindromic Subsequence.
* Memory Usage: 31.7 MB, less than 48.84% of Python3 online submissions for Longest Palindromic Subsequence.

> dp[i][j] = i~j最大回文長度
> 若s[i] == s[j] => dp[i][j] = 2+dp[i+1][j-1]
> 若s[i] != s[j] => 此時還是需要填入i~j最大回文長度，故挑選max(i~j-1, i-1~j)的最大值當作i~j的最大回文長度