Question: https://leetcode.com/problems/count-of-range-sum/

---

try_1.py: O(nlogn)
* Runtime: 1780 ms, faster than 5.03% of Python3 online submissions for Count of Range Sum.
* Memory Usage: 29.5 MB, less than 5.45% of Python3 online submissions for Count of Range Sum.

> 算出preSum之後，去找尋有幾個符合的preSum即可

---

try_2.py: O(n^2)
* TLE

> 先計算長度n，之後往右移動，dp把結果存起來，去查詢想要的結果即可
