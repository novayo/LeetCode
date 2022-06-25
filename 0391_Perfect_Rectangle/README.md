Question: https://leetcode.com/problems/perfect-rectangle/

---

try_1.py: O(n) O(n)

* Runtime: 656 ms, faster than 22.11% of Python3 online submissions for Perfect Rectangle.
* Memory Usage: 22.1 MB, less than 12.11% of Python3 online submissions for Perfect Rectangle.

> area + counter

---

try_2.py: O(nlogn) O(n)

* Runtime: 711 ms, faster than 15.46% of Python3 online submissions for Perfect Rectangle.
* Memory Usage: 20.2 MB, less than 32.99% of Python3 online submissions for Perfect Rectangle.

> sweep line + heap + greedy
> greedy: y找最遠，確認overlap
