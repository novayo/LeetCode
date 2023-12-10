Question: https://leetcode.com/problems/longest-palindromic-substring/
---

try_1.py: O(n^2)

* Runtime: 888 ms, faster than 86.47% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.

> straightforward = expand from center

---

try_2.py: O(n^2) O(n^2)

* Runtime: 8627 ms, faster than 7.89% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 22 MB, less than 12.45% of Python3 online submissions for Longest Palindromic Substring.

> dp[i][j] => 從i~j是否為回文 => 先初始化單個(dp[i][i] = True) => 之後開始找所有可能
> 若 s[i] != s[j] => 填False
> 若 s[i] == s[j] => 代表 a ..... a => 要確認是否dp[i+1][j-1] == True, 但還有 ..aa..的情況，故j-i+1 <= 2 or dp[i+1][j-1] == True => 就為回文 dp[i][j] = True

---

try_3.py: O(n^2) O(n)

* Runtime: 5468 ms, faster than 20.96% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 22.1 MB, less than 12.28% of Python3 online submissions for Longest Palindromic Substring.

> dp[i][j] = s[i~j] is palindrone

---

try_4.py: O(n^2) O(n)

* Runtime: 6872 ms, faster than 15.04% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 22.1 MB, less than 12.00% of Python3 online submissions for Longest Palindromic Substring.

> dp[i][j] = s[i~j] is palindrone

---

try_5.py: O(n) O(n)

* Runtime: 211 ms, faster than 95.09% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 14 MB, less than 75.61% of Python3 online submissions for Longest Palindromic Substring.

> manacher's algorithm

---

try_6.py: O(n^2) O(n)

* Runtime 322ms Beats 92.24%of users with Python3
* Memory 16.30MB Beats 74.27%of users with Python3

> expand around center

---

try_7.py: O(n^2) O(n^2)

* Runtime: 3396 ms, faster than 26.26% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 24.3 MB, less than 9.60% of Python3 online submissions for Longest Palindromic Substring.

> dp
