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
