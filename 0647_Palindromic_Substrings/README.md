Question: https://leetcode.com/problems/palindromic-substrings/

---

try_1.py: O(n^2) O(n)

* Runtime: 220 ms, faster than 49.96% of Python3 online submissions for Palindromic Substrings.
* Memory Usage: 22.1 MB, less than 27.39% of Python3 online submissions for Palindromic Substrings.

> dp[i][j] = i~j is palindrone

---

try_2.py: O(n) O(n)

* Runtime: 66 ms, faster than 99.09% of Python3 online submissions for Palindromic Substrings.
* Memory Usage: 13.9 MB, less than 79.07% of Python3 online submissions for Palindromic Substrings.

> manacher's algorithm