Question: https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

---

try_1.py: O(n) O(n)

* Runtime: 1576 ms, faster than 21.83% of Python3 online submissions for Maximum Subarray Sum After One Operation.
* Memory Usage: 35.2 MB, less than 15.85% of Python3 online submissions for Maximum Subarray Sum After One Operation.

> 記錄所有組合
> 沒平方過的 = max(上一個沒平方過的 + num, num)
> 有平方過的 = max(上一個沒平方過的 + num**2, 上一個平方過的 + num, num ** 2)