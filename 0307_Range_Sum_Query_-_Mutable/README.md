Question: https://leetcode.com/problems/range-sum-query-mutable/
---

try_1.py:

* Runtime: 716 ms, faster than 16.68% of Python3 online submissions for Range Sum Query - Mutable.
* Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Mutable.

> straightforward

---

try_2.py:

* Runtime: 1740 ms, faster than 68.75% of Python3 online submissions for Range Sum Query - Mutable.
* Memory Usage: 31.5 MB, less than 61.57% of Python3 online submissions for Range Sum Query - Mutable.

> binary index tree
> init - O(nlogn)
> update - O(logn)
> query - O(logn)

---

try_3.py: O(logn) O(n)

* Runtime: 1668 ms, faster than 64.23% of Python3 online submissions for Range Sum Query - Mutable.
* Memory Usage: 31.4 MB, less than 67.19% of Python3 online submissions for Range Sum Query - Mutable.

> binary indexed tree => partial sum
