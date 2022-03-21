Question: https://leetcode.com/problems/rotate-function/

---

try_1.py: O(n) O(1)

* Runtime: 1300 ms, faster than 91.71% of Python3 online submissions for Rotate Function.
* Memory Usage: 23.1 MB, less than 51.66% of Python3 online submissions for Rotate Function.

> f(i+1) = sum(A) + A[-1] * (-length) + f(i)