Question: https://leetcode.com/problems/lru-cache/

---

try_1.py:

* Runtime: 632 ms, faster than 12.61% of Python3 online submissions for LRU Cache.
* Memory Usage: 22.9 MB, less than 6.06% of Python3 online submissions for LRU Cache.

> intuition

---

try_2.py: O(1) O(capacity)

* Runtime: 1272 ms, faster than 25.80% of Python3 online submissions for LRU Cache.
* Memory Usage: 75.6 MB, less than 70.00% of Python3 online submissions for LRU Cache.

> using ordereddict => it's hashed but also ordered
> get and check the key => O(1)
> delete and move to the end => O(1)
> So use this feature to mimic lru cache

---

try_3.py: O(1) O(capacity)

* Runtime: 736 ms, faster than 95.27% of Python3 online submissions for LRU Cache.
* Memory Usage: 76.4 MB, less than 34.91% of Python3 online submissions for LRU Cache.

> ordereddict
