Question: https://leetcode.com/problems/132-pattern/

---

try_1.py: O(n^2) O(1)

* TLE

> 用two pointer模擬找尋過程，左邊則直接紀錄最小

---

try_2.py: O(n) O(n)

* Runtime: 376 ms, faster than 46.23% of Python3 online submissions for 132 Pattern.
* Memory Usage: 32.5 MB, less than 10.00% of Python3 online submissions for 132 Pattern.

> 邊找邊剔除右邊不需要參考的值即可
