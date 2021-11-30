Question: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
---

try_1.py: O(n*x) 872ms

* Runtime: 960 ms, faster than 5.04% of Python3 online submissions for Longest Word in Dictionary through Deleting.
* Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Longest Word in Dictionary through Deleting.

> straightforward

---

try_2.py: O(n*log(x))

* Runtime: 112 ms, faster than 89.81% of Python3 online submissions for Longest Word in Dictionary through Deleting.
* Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Longest Word in Dictionary through Deleting.

> binary search

---

try_3.py: O(len(s)^2) O(n)

* TLE

> bfs

---

try_4.py: O(nlogn) O(n)

* Runtime: 212 ms, faster than 77.80% of Python3 online submissions for Longest Word in Dictionary through Deleting.
* Memory Usage: 16.4 MB, less than 99.22% of Python3 online submissions for Longest Word in Dictionary through Deleting.

> sort dictionary by length(bucket sort) and two pointer 
