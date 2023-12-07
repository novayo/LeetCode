Question: https://leetcode.com/problems/maximal-square/

---

try_1.py:
* Runtime: 232 ms, faster than 35.06% of Python3 online submissions for Maximal Square.
* Memory Usage: 18.1 MB, less than 9.09% of Python3 online submissions for Maximal Square.

> dp

---

try_2.py: O(m*n)

* Runtime: 274 ms, faster than 38.37% of Python3 online submissions for Maximal Square.
* Memory Usage: 15.5 MB, less than 75.27% of Python3 online submissions for Maximal Square.

> 3*3 要保證 上的2*2 & 左的2*2 & 左上的2*2 皆為正方形 & 本身是1 => 才會是3*3
> 但有可能 左上是4*4，此點是3*3 => 因此三方向要挑最小的出來+1

---

try_3.py: O(n) O(n)

* Runtime: 224 ms, faster than 49.94% of Python3 online submissions for Maximal Square.
* Memory Usage: 16.8 MB, less than 12.67% of Python3 online submissions for Maximal Square.

> dp

---

try_4.py: O(mn) O(1)

* Runtime: 613 ms, faster than 52.06% of Python3 online submissions for Maximal Square.
* Memory Usage: 19.4 MB, less than 38.38% of Python3 online submissions for Maximal Square.

> dp
