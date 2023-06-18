Question: https://leetcode.com/problems/find-peak-element/

---

try_1.py: O(n)

* Runtime: 96 ms, faster than 5.17% of Python3 online submissions for Find Peak Element.
* Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Find Peak Element.

> find smaller one, return the first

---

try_2.py: O(logn)

* Runtime: 40 ms, faster than 91.01% of Python3 online submissions for Find Peak Element.
* Memory Usage: 14.2 MB, less than 5.88% of Python3 online submissions for Find Peak Element.

> binary search
	> 隨便切一個點，往峰值前進，用binary search縮減找尋時間
	> https://i.imgur.com/WpgzYqW.png
---

try_3.py: O(logn)

* Runtime: 44 ms, faster than 77.73% of Python3 online submissions for Find Peak Element.
* Memory Usage: 14.5 MB, less than 11.34% of Python3 online submissions for Find Peak Element.

> July Challenge: binary search

---

try_4.py: O(logn) O(1)

* Runtime: 36 ms, faster than 98.57% of Python3 online submissions for Find Peak Element.
* Memory Usage: 14.3 MB, less than 72.10% of Python3 online submissions for Find Peak Element.

> binary search

---

try_5.py: O(logn) O(1)

* Runtime: 54 ms, faster than 82.00% of Python3 online submissions for Find Peak Element.
* Memory Usage: 16.6 MB, less than 24.33% of Python3 online submissions for Find Peak Element.

> binary search