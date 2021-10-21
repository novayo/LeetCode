Question: https://leetcode.com/problems/house-robber-ii/

---

try_1.py: O(nlogn) O(n)

* Runtime: 32 ms, faster than 74.56% of Python3 online submissions for House Robber II.
* Memory Usage: 14.3 MB, less than 24.34% of Python3 online submissions for House Robber II.

> using heapq to maintain max[0~index] and find max(0~n-1, 1~n)

---

try_2.py: O(n) O(n)

* Runtime: 36 ms, faster than 45.23% of Python3 online submissions for House Robber II.
* Memory Usage: 14.4 MB, less than 24.34% of Python3 online submissions for House Robber II.

> using dp to memo max[0~index] and find max(0~n-1, 1~n)
