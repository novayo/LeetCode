Question: https://leetcode.com/problems/minimum-height-trees/

---

try_1.py: O(n) O(n)

* Runtime: 333 ms, faster than 24.74% of Python3 online submissions for Minimum Height Trees.
* Memory Usage: 19.2 MB, less than 24.91% of Python3 online submissions for Minimum Height Trees.

> 一層一層往上找，最下層只有一個指向他，去除最下層的同時，更新爸爸的children進而找到下一個leaf => topological sort

---

try_2.py: O(n) O(n)

* Runtime: 791 ms, faster than 20.57% of Python3 online submissions for Minimum Height Trees.
* Memory Usage: 24.9 MB, less than 32.00% of Python3 online submissions for Minimum Height Trees.

> topological sort
