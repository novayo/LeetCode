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

---

try_4.py: O(m*n) O(m*n)

* Runtime: 1413 ms, faster than 13.13% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 140.3 MB, less than 15.15% of Python3 online submissions for Longest Common Subsequence.

> 慢慢往前找

---

try_5.py: O(mn) O(mn)

* Runtime: 2318 ms, faster than 5.01% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 480.4 MB, less than 5.67% of Python3 online submissions for Longest Common Subsequence.

> recursion

---

try_6.py: O(mn) O(mn)

* Runtime: 954 ms, faster than 26.06% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 41.8 MB, less than 58.53% of Python3 online submissions for Longest Common Subsequence.

> dp

---

try_7.py: O(mn) O(min(m, n))

* Runtime: 783 ms, faster than 34.05% of Python3 online submissions for Longest Common Subsequence.
* Memory Usage: 16.3 MB, less than 97.53% of Python3 online submissions for Longest Common Subsequence.

> dp (space optimize)
