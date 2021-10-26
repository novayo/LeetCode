Question: https://leetcode.com/problems/house-robber/

---

try_1.py: O(n^2)
* Runtime: 36 ms, faster than 17.85% of Python3 online submissions for House Robber.
* Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.

> recr + dp

---

try_2.py: O(n^2)
* Runtime: 28 ms, faster than 76.12% of Python3 online submissions for House Robber. 
* Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for House Robber.

> button-up

---

try_3.py: O(n) O(1)

* Runtime: 43 ms, faster than 30.70% of Python3 online submissions for House Robber.
* Memory Usage: 14.3 MB, less than 19.57% of Python3 online submissions for House Robber.

> 從index=2開始，往前找0~index-2的最大，從這點走到index就會為最大值

---

try_4.py: O(n) O(1)

* Runtime: 32 ms, faster than 75.96% of Python3 online submissions for House Robber.
* Memory Usage: 14.3 MB, less than 19.77% of Python3 online submissions for House Robber.

> state dp