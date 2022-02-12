Question: https://leetcode.com/problems/find-k-closest-elements/

---

try_1.py: O(logn)
* Runtime: 304 ms, faster than 91.41% of Python3 online submissions for Find K Closest Elements.
* Memory Usage: 15 MB, less than 95.57% of Python3 online submissions for Find K Closest Elements.

> binary search 

---

try_2.py: O(logn + k)

* Runtime: 296 ms, faster than 67.96% of Python3 online submissions for Find K Closest Elements.
* Memory Usage: 15.6 MB, less than 69.77% of Python3 online submissions for Find K Closest Elements.

> binary search to find lower bound

---

try_3.py: O(logn + k) O(1)

* Runtime: 512 ms, faster than 24.03% of Python3 online submissions for Find K Closest Elements.
* Memory Usage: 15.5 MB, less than 87.34% of Python3 online submissions for Find K Closest Elements.

> bisect left + lower bound
