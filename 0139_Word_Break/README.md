Question: https://leetcode.com/problems/word-break/
---

try_1.py: O(n)

* Runtime: 24 ms, faster than 99.84% of Python3 online submissions for Word Break.
* Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Break.

> straightforward

---

try_2.py:
* Runtime: 16 ms, faster than 100.00% of Python3 online submissions for Word Break.
* Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Word Break.

> bfs with dp

---

try_3.py: O(n^2) O(n)

* Runtime: 44 ms, faster than 51.81% of Python3 online submissions for Word Break.
* Memory Usage: 14.3 MB, less than 70.94% of Python3 online submissions for Word Break.

> dp[i] => 0~i 是合格的

---

try_4.py: O(n*m) O(n)

* Runtime: 43 ms, faster than 64.96% of Python3 online submissions for Word Break.
* Memory Usage: 16.2 MB, less than 87.46% of Python3 online submissions for Word Break.

> dp
