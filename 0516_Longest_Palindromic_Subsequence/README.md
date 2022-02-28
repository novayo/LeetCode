Question: https://leetcode.com/problems/longest-palindromic-subsequence/

---

try_1.py: O(n^2) O(n^2)

* Runtime: 2811 ms, faster than 33.13% of Python3 online submissions for Longest Palindromic Subsequence.
* Memory Usage: 31.7 MB, less than 48.84% of Python3 online submissions for Longest Palindromic Subsequence.

> dp[i][j] = i~j最大回文長度
> 若s[i] == s[j] => dp[i][j] = 2+dp[i+1][j-1]
> 若s[i] != s[j] => 此時還是需要填入i~j最大回文長度，故挑選max(i~j-1, i-1~j)的最大值當作i~j的最大回文長度

---

try_2.py: O(n^2) O(n^2)

* Runtime: 1440 ms, faster than 72.50% of Python3 online submissions for Longest Palindromic Subsequence.
* Memory Usage: 30.6 MB, less than 85.59% of Python3 online submissions for Longest Palindromic Subsequence.

> dp[i][j] => s[i:j]有幾個回文

---

try_3.py: O(n^2) O(n^2)

* Runtime: 1559 ms, faster than 79.54% of Python3 online submissions for Longest Palindromic Subsequence.
* Memory Usage: 249.9 MB, less than 13.11% of Python3 online submissions for Longest Palindromic Subsequence.

> recursion

---

try_4.py: O(n^2) O(n^2)

* Runtime: 2421 ms, faster than 48.40% of Python3 online submissions for Longest Palindromic Subsequence.
* Memory Usage: 30.6 MB, less than 74.73% of Python3 online submissions for Longest Palindromic Subsequence.

> dp
