Question: https://leetcode.com/problems/min-cost-climbing-stairs/

---

try_1.py: O(n) O(1)

* Runtime: 59 ms, faster than 65.13% of Python3 online submissions for Min Cost Climbing Stairs.
* Memory Usage: 14.6 MB, less than 21.37% of Python3 online submissions for Min Cost Climbing Stairs.

> dp => 往前挑兩個挑最小的去加即可，最後回傳倒數兩個最小(因為都可以跳到最後)，起始是第一、第二不動