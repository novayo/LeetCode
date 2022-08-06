Question: https://leetcode.com/problems/number-of-matching-subsequences/

---

try_1.py: O(len(s)^2) O(len(s)^2)

* TLE

> bfs set

---

try_2.py: O(len(words) * len(word) * log(len(s))) O(len(words))

* Runtime: 596 ms, faster than 56.06% of Python3 online submissions for Number of Matching Subsequences.
* Memory Usage: 17.4 MB, less than 12.04% of Python3 online submissions for Number of Matching Subsequences.

> binary search and cache

---

try_2.py: O(len(s) * 2) O(len(s))

* Runtime: 2538 ms, faster than 22.10% of Python3 online submissions for Number of Matching Subsequences.
* Memory Usage: 20.6 MB, less than 6.58% of Python3 online submissions for Number of Matching Subsequences.

> keep found index
