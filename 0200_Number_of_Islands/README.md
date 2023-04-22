Question: https://leetcode.com/problems/number-of-islands/
---

try_1.py: O(m * n) 136ms

* Runtime: 136 ms, faster than 94.77% of Python3 online submissions for Number of Islands.
* Memory Usage: 13.8 MB, less than 75.21% of Python3 online submissions for Number of Islands.

> using dfs to loop four directions

---

try_2.cpp: O(m*n)

* Runtime: 32 ms, faster than 98.21% of C++ online submissions for Number of Islands.
* Memory Usage: 12.4 MB, less than 55.86% of C++ online submissions for Number of Islands.

> dfs
        
---

try_3.py: O(m*b)

* Runtime: 288 ms, faster than 93.06% of Python3 online submissions for Number of Islands.
* Memory Usage: 16.2 MB, less than 97.75% of Python3 online submissions for Number of Islands.

> bfs

---

try_4.py: O(mnlogn)

* Runtime: 455 ms, faster than 50.34% of Python3 online submissions for Number of Islands.
* Memory Usage: 25.9 MB, less than 5.57% of Python3 online submissions for Number of Islands.

> union find

---

try_5.py: O(mn) O(mn)

* Runtime: 285 ms, faster than 91.52% of Python3 online submissions for Number of Islands.
* Memory Usage: 16.2 MB, less than 91.55% of Python3 online submissions for Number of Islands.

> bfs level order traversal

---

try_6.py: O(mn) O(mn)

* Runtime: 282 ms, faster than 83.52% of Python3 online submissions for Number of Islands.
* Memory Usage: 16.4 MB, less than 79.47% of Python3 online submissions for Number of Islands.

> dfs, bfs