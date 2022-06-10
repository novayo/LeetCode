Question: https://leetcode.com/problems/trapping-rain-water/

---

try_1.py: O(n)

* Runtime: 32 ms, faster than 99.98% of Python3 online submissions for Trapping Rain Water.
* Memory Usage: 13.3 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.

> straightforward = Using 2 pointers

---

try_2.py: O(2n)

* Runtime: 52 ms, faster than 82.51% of Python3 online submissions for Trapping Rain Water.
* Memory Usage: 14.9 MB, less than 68.24% of Python3 online submissions for Trapping Rain Water.

> Monotonic Stack的概念，遇到大於等於的就結算之前的起點，但最後可能有剩餘的，就反過來再做一次。

---

try_3.py: O(2n) O(n)

* Runtime: 60 ms, faster than 44.71% of Python3 online submissions for Trapping Rain Water.
* Memory Usage: 14.8 MB, less than 68.24% of Python3 online submissions for Trapping Rain Water.

> monotonic stack: push index

---

try_4.py: O(2n) O(n)

* Runtime: 56 ms, faster than 61.34% of Python3 online submissions for Trapping Rain Water.
* Memory Usage: 14.8 MB, less than 87.29% of Python3 online submissions for Trapping Rain Water.

> 每次計算i, bot, j中間的差值即可

---

try_5.py: O(n) O(n)

* Runtime: 158 ms, faster than 47.86% of Python3 online submissions for Trapping Rain Water.
* Memory Usage: 16 MB, less than 41.91% of Python3 online submissions for Trapping Rain Water.

> dp
