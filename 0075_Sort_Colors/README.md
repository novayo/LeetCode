Question: https://leetcode.com/problems/sort-colors/

---

try_1.py:
* Runtime: 32 ms, faster than 69.55% of Python3 online submissions for Sort Colors.
* Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Sort Colors.

> binary search

---

try_2.py: O(n) O(1)

* Runtime: 36 ms, faster than 51.70% of Python3 online submissions for Sort Colors.
* Memory Usage: 14.3 MB, less than 46.21% of Python3 online submissions for Sort Colors.

> use two pointer
> must satisfy the following two condition
> 	1. i <= k <= j
> 	2. when nums[k] == 1 => then k moves
