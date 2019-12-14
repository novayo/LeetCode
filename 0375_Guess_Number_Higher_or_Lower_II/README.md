Question: https://leetcode.com/problems/guess-number-higher-or-lower-ii/

---

try_1.py:
* Runtime: 688 ms, faster than 59.72% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 32.5 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> dp + recursive

---

try_2.py:
* Runtime: 296 ms, faster than 90.00% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 32.4 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> optimize try_1.py
> 	* if find out left_max > right_max, then break the loop
> 	* because loop 從左邊到右邊，那左邊的值會漸漸的大於右邊，因此，之後的loop也會一直左邊大於右邊，那就沒有再loop的必要了，因此可以break

---

try_3.py:
* Runtime: 96 ms, faster than 96.20% of Python3 online submissions for Guess Number Higher or Lower II.
* Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.

> optimize try_2.py
> 	* using dictionary instead of array
