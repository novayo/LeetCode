Question: https://leetcode.com/problems/largest-divisible-subset/

---

try_1.py: O(n^2) O(n)

* Runtime: 296 ms, faster than 95.32% of Python3 online submissions for Largest Divisible Subset.
* Memory Usage: 14.3 MB, less than 94.88% of Python3 online submissions for Largest Divisible Subset.

> 排序好後，每個index 找 之前list中最大的數值 % == 0 => 代表跟此list其餘的也可以整除
