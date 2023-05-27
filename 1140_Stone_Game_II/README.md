Question: https://leetcode.com/problems/stone-game-ii/

---

try_1.py: O(n^2) O(n)
* Runtime: 428 ms, faster than 38.14% of Python3 online submissions for Stone Game II.
* Memory Usage: 15.9 MB, less than 39.71% of Python3 online submissions for Stone Game II.

> 此recr為，下一個人選擇的剩下的最大值，因為Alex先選，所以sum()-recr為Alice去減掉(Bob所選擇的最大可能)

---

try_2.py: O(n^2) O(n)

* Runtime: 1868 ms, faster than 10.60% of Python3 online submissions for Stone Game II.
* Memory Usage: 17.6 MB, less than 23.13% of Python3 online submissions for Stone Game II.

> recr => Alice score

---

try_3.py: O(n^2) O(n)

* Runtime: 698 ms, faster than 41.04% of Python3 online submissions for Stone Game II.
* Memory Usage: 20.3 MB, less than 20.75% of Python3 online submissions for Stone Game II.

> min / max recursion
