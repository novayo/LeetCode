Question: https://leetcode.com/problems/uncrossed-lines/

---

try_1.py: O(n^2) O(n)

* Runtime: 308 ms, faster than 28.22% of Python3 online submissions for Uncrossed Lines.
* Memory Usage: 19 MB, less than 15.33% of Python3 online submissions for Uncrossed Lines.

> https://drive.google.com/file/d/1o2NqwVBJmcem0UWwELIY3GbwdqO1l47G/view?usp=sharing

---

try_2.py: O(m*n) O(m*n)

* Runtime: 188 ms, faster than 87.81% of Python3 online submissions for Uncrossed Lines.
* Memory Usage: 14.7 MB, less than 44.10% of Python3 online submissions for Uncrossed Lines.

>劉 dp[i][j] = nums1[i:], nums2[j:] 的最多條線

---

try_3.py: O(m*n) O(m*n)

* Runtime: 230 ms, faster than 58.02% of Python3 online submissions for Uncrossed Lines.
* Memory Usage: 14.6 MB, less than 58.38% of Python3 online submissions for Uncrossed Lines.

> 討論dp[i][j] = s[:i] t[:j] 的所有情況
