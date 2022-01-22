Question: https://leetcode.com/problems/longest-common-subsequence/

---

try_1.py: O(m*n) O(m*n)

* Runtime: 475 ms, faster than 53.93% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 22.9 MB, less than 39.74% of Python3 online submissions for Longest Common Subsequence.

> https://i.imgur.com/6Hpse82.png
> 利用這種dp去記錄每個已經有重複多少了，同時只要當前記錄最大的即可

---

try_2.py: O(m*n) O(m*n)

* Runtime: 420 ms, faster than 72.57% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 22 MB, less than 67.92% of Python3 online submissions for Longest Common Subsequence.

> 紀錄之前已經有出現過幾個

---

try_3.py: O(m*n) O(m*n)

* Runtime: 488 ms, faster than 56.63% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 22.1 MB, less than 71.92% of Python3 online submissions for Longest Common Subsequence.

> LCS dp
