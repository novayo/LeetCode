Question: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

---

try_1.py: O(n^2*logn) O(n)

* Runtime: 5136 ms, faster than 20.73% of Python3 online submissions for Count of Smaller Numbers After Self.
* Memory Usage: 32.6 MB, less than 85.00% of Python3 online submissions for Count of Smaller Numbers After Self.

> binary search to handle sorted list and find number of smaller elements

---

try_2.py: O(nlogn) O(n)

* Runtime: 2484 ms, faster than 68.29% of Python3 online submissions for Count of Smaller Numbers After Self.
* Memory Usage: 35.3 MB, less than 37.40% of Python3 online submissions for Count of Smaller Numbers After Self.

> binary indexed tree to optimize try_1.py
