Question: https://leetcode.com/problems/find-latest-group-of-size-m/

---

try_1.py: O(nlogn) O(n)

* Runtime: 3570 ms, faster than 5.89% of Python3 online submissions for Find Latest Group of Size M.
* Memory Usage: 39.7 MB, less than 9.41% of Python3 online submissions for Find Latest Group of Size M.

> union find

---

try_2.py: O(n) O(n)

* Runtime: 960 ms, faster than 96.47% of Python3 online submissions for Find Latest Group of Size M.
* Memory Usage: 27.9 MB, less than 86.47% of Python3 online submissions for Find Latest Group of Size M.

> 只要union左右兩邊即可，所以只需要更新邊界的新長度即可