Question: https://leetcode.com/problems/minimum-path-sum/

---

try_1.py: O(m*n)
* Runtime: 92 ms, faster than 97.03% of Python3 online submissions for Minimum Path Sum.
* Memory Usage: 15.2 MB, less than 26.32% of Python3 online submissions for Minimum Path Sum.

> based on Q62 but min(up, left)

---

try_2.py: O(m*n)

* Runtime: 144 ms, faster than 26.40% of Python3 online submissions for Minimum Path Sum.
* Memory Usage: 15.7 MB, less than 63.42% of Python3 online submissions for Minimum Path Sum.

> 上右挑小的累加即可

---

try_3.py: O(m*n)

* Runtime: 100 ms, faster than 70.28% of Python3 online submissions for Minimum Path Sum.
* Memory Usage: 15.6 MB, less than 81.82% of Python3 online submissions for Minimum Path Sum.

> dp

---

try_4.py: O(n) O(1)

* Runtime: 132 ms, faster than 26.58% of Python3 online submissions for Minimum Path Sum.
* Memory Usage: 15.7 MB, less than 63.73% of Python3 online submissions for Minimum Path Sum.

> dp
