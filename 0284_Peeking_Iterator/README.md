Question: https://leetcode.com/problems/peeking-iterator/

---

try_1.py: O(1) O(n)

* Runtime: 50 ms, faster than 9.44% of Python3 online submissions for Peeking Iterator.
* Memory Usage: 14.3 MB, less than 86.82% of Python3 online submissions for Peeking Iterator.

> saving peeked element

---

try_2.py: O(1) O(1)

* Runtime: 34 ms, faster than 33.59% of Python3 online submissions for Peeking Iterator.
* Memory Usage: 14.5 MB, less than 29.55% of Python3 online submissions for Peeking Iterator.

> save next 
> => when peek() => return next
> => when next() => save next peek and return cur peek

---

try_3.py: O(1) O(1)

* Runtime: 32 ms, faster than 66.74% of Python3 online submissions for Peeking Iterator.
* Memory Usage: 14.5 MB, less than 29.53% of Python3 online submissions for Peeking Iterator.

> peek next
