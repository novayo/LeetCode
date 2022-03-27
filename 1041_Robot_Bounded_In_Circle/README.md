Question: https://leetcode.com/problems/robot-bounded-in-circle/

---

try_1.py: O(n) O(1)

* Runtime: 24 ms, faster than 95.92% of Python3 online submissions for Robot Bounded In Circle.
* Memory Usage: 14.2 MB, less than 75.33% of Python3 online submissions for Robot Bounded In Circle.

> loop through once and check out if
> 	back to initial point
> 	face != UP

---

try_2.py: O(n) O(1)

* Runtime: 39 ms, faster than 65.87% of Python3 online submissions for Robot Bounded In Circle.
* Memory Usage: 13.9 MB, less than 76.86% of Python3 online submissions for Robot Bounded In Circle.

> 走四次，每走完一個instruction再判斷是否回到原點&面向上
