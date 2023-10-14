Question: https://leetcode.com/problems/range-sum-query-immutable/

---

try_1.py: O(n) o(n)
* Runtime: 68 ms, faster than 97.35% of Python3 online submissions for Range Sum Query - Immutable.
* Memory Usage: 17.8 MB, less than 13.88% of Python3 online submissions for Range Sum Query - Immutable.

> dp: 累加起來，這樣dp[i]-dp[j]就代表i加到j的總和

---

try_2.py: O(n) O(n)

* Runtime: 79 ms, faster than 88.66% of Python3 online submissions for Range Sum Query - Immutable.
* Memory Usage: 20 MB, less than 26.17% of Python3 online submissions for Range Sum Query - Immutable.

> presum

---

try_3.py: O(10**4 * n) O(n)

* Runtime: 3497 ms, faster than 8.31% of Python3 online submissions for Range Sum Query - Immutable.
* Memory Usage: 19.7 MB, less than 83.54% of Python3 online submissions for Range Sum Query - Immutable.

> normal
