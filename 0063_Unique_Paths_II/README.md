Question: https://leetcode.com/problems/unique-paths-ii/

---

try_1.py: O(m*n)
* Runtime: 40 ms, faster than 91.84% of Python3 online submissions for Unique Paths II.
* Memory Usage: 13.8 MB, less than 8.89% of Python3 online submissions for Unique Paths II.

> dp

---

try_2.py: O(m*n)

* Runtime: 44 ms, faster than 68.83% of Python3 online submissions for Unique Paths II.
* Memory Usage: 14.3 MB, less than 83.59% of Python3 online submissions for Unique Paths II.

> dp，上左遇到石頭時則+0，要先處理第一行跟第一列，有石頭則後續的皆為0(走不到)