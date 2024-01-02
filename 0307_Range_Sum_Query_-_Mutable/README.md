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

---

try_4.py: O(logn) O(n)

* Runtime: 6290 ms, faster than 5.02% of Python3 online submissions for Range Sum Query - Mutable.
* Memory Usage: 49.6 MB, less than 25.76% of Python3 online submissions for Range Sum Query - Mutable.

> segment tree to find range sum

---

try_5.py: O(logn) O(n)

* Runtime: 2646 ms, faster than 50.95% of Python3 online submissions for Range Sum Query - Mutable.
* Memory Usage: 31.6 MB, less than 58.90% of Python3 online submissions for Range Sum Query - Mutable.

> bit to find range sum

---

try_6.py: O(logn) O(n)

* Runtime 4517ms Beats 6.34%of users with Python3
* Memory 49.52MB Beats 23.24%of users with Python3

> segment tree
