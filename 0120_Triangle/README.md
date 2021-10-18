Question: https://leetcode.com/problems/triangle/

---

try_1.py: O(n) O(n)

* Runtime: 68 ms, faster than 22.95% of Python3 online submissions for Triangle.
* Memory Usage: 17 MB, less than 7.59% of Python3 online submissions for Triangle.

> recursion + memo

---

try_2.py: O(n) O(1)

* Runtime: 48 ms, faster than 98.49% of Python3 online submissions for Triangle.
* Memory Usage: 14.8 MB, less than 7.59% of Python3 online submissions for Triangle.

> dp
> 把左右兩邊整條加起來之後，就會轉成帕斯卡三角形了

---

try_3.py: O(n) O(1)

* Runtime: 64 ms, faster than 76.38% of Python3 online submissions for Triangle.
* Memory Usage: 14.9 MB, less than 90.72% of Python3 online submissions for Triangle.

> buttom-up in place