Question: https://leetcode.com/problems/insert-delete-getrandom-o1/

---

try_1.py: O(n) O(n)

* Runtime: 444 ms, faster than 9.10% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 18.9 MB, less than 7.21% of Python3 online submissions for Insert Delete GetRandom O(1).

> getRandom 為 O(n)

---

try_2.py: O(1) O(n)

* Runtime: 92 ms, faster than 87.68% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 18.5 MB, less than 60.25% of Python3 online submissions for Insert Delete GetRandom O(1).

> list存值，dict存key=值，value=index，因此只要取亂數時，從list取就好，但remove要注意list跟dict的index要同步