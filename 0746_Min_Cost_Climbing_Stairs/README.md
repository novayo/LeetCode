Question: https://leetcode.com/problems/min-cost-climbing-stairs/

---

try_1.py: O(n) O(1)

* Runtime: 59 ms, faster than 65.13% of Python3 online submissions for Min Cost Climbing Stairs.
* Memory Usage: 14.6 MB, less than 21.37% of Python3 online submissions for Min Cost Climbing Stairs.

> dp => 往前挑兩個挑最小的去加即可，最後回傳倒數兩個最小(因為都可以跳到最後)，起始是第一、第二不動

---

try_2.py: O(n) O(1)

* Runtime: 112 ms, faster than 16.50% of Python3 online submissions for Min Cost Climbing Stairs.
* Memory Usage: 14.1 MB, less than 37.86% of Python3 online submissions for Min Cost Climbing Stairs.

> dp

---

try_3.py: O(n) O(n)

* Runtime: 59 ms, faster than 73.47% of Python3 online submissions for Min Cost Climbing Stairs.
* Memory Usage: 18.7 MB, less than 11.12% of Python3 online submissions for Min Cost Climbing Stairs.

> recr + memo

---

try_4.py: O(n) O(n)

* Runtime: 67 ms, faster than 32.24% of Python3 online submissions for Min Cost Climbing Stairs.
* Memory Usage: 16.5 MB, less than 63.35% of Python3 online submissions for Min Cost Climbing Stairs.

> dp
