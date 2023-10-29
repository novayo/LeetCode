Runtime: 1619 ms, faster than 33.66% of Python3 online submissions for Partition Equal Subset Sum.
Question: https://leetcode.com/problems/combination-sum-iv/

---

try_1.py: O(n*target) O(target)

* Runtime: 74 ms, faster than 10.46% of Python3 online submissions for Combination Sum IV.
* Memory Usage: 14.1 MB, less than 89.09% of Python3 online submissions for Combination Sum IV.

> coin2 (but with coin loop inside)，因為(1,2) (2,1)要分開算

---

try_2.py: O(n*target) O(target)

* Runtime: 89 ms, faster than 9.44% of Python3 online submissions for Combination Sum IV.
* Memory Usage: 14.1 MB, less than 32.12% of Python3 online submissions for Combination Sum IV.

> recursion

---

try_3.py: O(n*target) O(target)

* Runtime: 87 ms, faster than 10.59% of Python3 online submissions for Combination Sum IV.
* Memory Usage: 13.9 MB, less than 83.60% of Python3 online submissions for Combination Sum IV.

> dp

---

try_4.py: O(n*target) O(n*target)

* Runtime: 46 ms, faster than 52.99% of Python3 online submissions for Combination Sum IV.
* Memory Usage: 16.4 MB, less than 57.21% of Python3 online submissions for Combination Sum IV.

> dp
