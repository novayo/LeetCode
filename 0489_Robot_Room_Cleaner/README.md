Question: https://leetcode.com/problems/robot-room-cleaner/

---

try_1.py:
* Runtime: 72 ms, faster than 66.61% of Python3 online submissions for Robot Room Cleaner.
* Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Robot Room Cleaner.

> dfs

---

try_2.py:
* Runtime: 64 ms, faster than 96.24% of Python3 online submissions for Robot Room Cleaner.
* Memory Usage: 15.3 MB, less than 20.07% of Python3 online submissions for Robot Room Cleaner.

> backtrack
> 若四個方向都走過了就backtrack，回到上一個狀態(面對的方向)

---

try_3.py: O(N-M) O(N-M) - where N is the number of cells and M is the number of obstacles 

* Runtime: 123 ms, faster than 21.34% of Python3 online submissions for Robot Room Cleaner.
* Memory Usage: 16.6 MB, less than 5.35% of Python3 online submissions for Robot Room Cleaner.

> backtracking
