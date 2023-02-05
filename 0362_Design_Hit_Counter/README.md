Question: https://leetcode.com/problems/design-hit-counter/

---

try_1.py:
* Runtime: 28 ms, faster than 73.41% of Python3 online submissions for Design Hit Counter.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Design Hit Counter.

> using set dictionary to store timestamp

---

try_2.py:
* Runtime: 24 ms, faster than 91.10% of Python3 online submissions for Design Hit Counter.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Design Hit Counter.

> optimize try_1.py

---

try_3.py:
* Runtime: 16 ms, faster than 99.89% of Python3 online submissions for Design Hit Counter.
* Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Design Hit Counter.

> using only dictionary to store timestamp

---

try_4.py:

* Runtime: 32 ms, faster than 66.49% of Python3 online submissions for Design Hit Counter.
* Memory Usage: 14.1 MB, less than 91.50% of Python3 online submissions for Design Hit Counter.

> take a list to store timestamp, when get_hit -> perform a binary search
> take a dict to store hit counter at timestamp
            
---

try_5.py: O(nlogn) / O(n) - where n is the number of api calls.

* Runtime: 25 ms, faster than 96.51% of Python3 online submissions for Design Hit Counter.
* Memory Usage: 13.9 MB, less than 95.76% of Python3 online submissions for Design Hit Counter.

> binary search right
