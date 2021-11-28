Question: https://leetcode.com/problems/bomb-enemy/

---

try_1.py: O(n) O(n)

* Runtime: 756 ms, faster than 62.80% of Python3 online submissions for Bomb Enemy.
* Memory Usage: 19.5 MB, less than 43.40% of Python3 online submissions for Bomb Enemy.

> do cache

---

try_2,py: O(n) O(n)

* Runtime: 1184 ms, faster than 14.31% of Python3 online submissions for Bomb Enemy.
* Memory Usage: 19.5 MB, less than 44.01% of Python3 online submissions for Bomb Enemy.

> optimize try_1.py
> 	1. rowCount => use int variable instead of dictionary
> 	2. remain colTable as dictionary to prevent sparse matrix