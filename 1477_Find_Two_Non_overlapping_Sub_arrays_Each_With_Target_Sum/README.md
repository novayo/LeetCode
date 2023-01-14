Question: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

---

try_1.py: O(n) O(n)

* Runtime: 1148 ms, faster than 35.53% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.
* Memory Usage: 28.2 MB, less than 73.31% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.

> dp prefix & suffix means at index i, the minimum length of answer is dp[i]

---

try_2.py: O(n) O(n)

* Runtime: 998 ms, faster than 76.14% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.
* Memory Usage: 36.9 MB, less than 22.73% of Python3 online submissions for Find Two Non-overlapping Sub-arrays Each With Target Sum.

> prefix + hash + dp
