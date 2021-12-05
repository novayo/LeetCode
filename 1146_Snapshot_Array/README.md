Question: https://leetcode.com/problems/snapshot-array/

---

try_1.py: O(logn) O(n)

* Runtime: 590 ms, faster than 23.47% of Python3 online submissions for Snapshot Array.
* Memory Usage: 38.8 MB, less than 43.02% of Python3 online submissions for Snapshot Array.

> if we want to memorize changes only, we can use binary search to find the rest number in array (once we don't store the snap=2 in index=2 => we still can find snap=1 by binary search)

---

try_2.py: O(1) O(n)

* Runtime: 396 ms, faster than 84.89% of Python3 online submissions for Snapshot Array.
* Memory Usage: 34.7 MB, less than 53.94% of Python3 online submissions for Snapshot Array.

> dict to prevent sparse matrix
