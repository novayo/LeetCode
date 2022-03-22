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

---

try_3.py: O(n) O(n)

* Runtime: 53 ms, faster than 10.42% of Python3 online submissions for House Robber II.
* Memory Usage: 14.4 MB, less than 25.78% of Python3 online submissions for House Robber II.

> 基本型I

---

try_4.py: O(n) O(1)

* Runtime: 58 ms, faster than 22.34% of Python3 online submissions for House Robber II.
* Memory Usage: 13.9 MB, less than 36.66% of Python3 online submissions for House Robber II.

> dp